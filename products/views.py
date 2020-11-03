from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, ProductForm, CategoryForm

from django.http import HttpResponse
from django.template import loader

from .models import Product, Category
from django.db import transaction
from django.http import JsonResponse
from django.contrib.auth.models import User
import datetime
from django.contrib import messages


def home(request):
    product_list = Product.objects.all()
    category_list = Category.objects.all()
    context = {
        'product_list': product_list,
        'category_list': category_list,
    }
    return render(request, 'home.html', context)


def signup(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        # form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
        else:
            messages.error(request, form.errors)
            # return redirect('home')
    
    return render(request, 'signup.html', {'form': form})


def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = auth_login(request, user)
            print('user logged in')
            return redirect('home')
        else:
            messages.error(request,form.errors)
            print('Account does not exists. Please try to sign in again')

    
    return render(request, 'login.html', {'form': form, 'title': 'log in'})


def product(request):
    template = loader.get_template('product.html')
    if request.method == 'GET':
        product_list = Product.objects.all()
        category_list = Category.objects.all()
        context = {
            'product_list': product_list,
            'category_list': category_list,
        }
    return HttpResponse(template.render(context, request))


def update_product(request, p_id):
    template = loader.get_template('update_product.html')
    if request.method == 'GET':
        product = Product.objects.get(id=p_id)
        category_list = Category.objects.all()
        user_list = User.objects.all()
        context = {
            'product': product,
            'category_list': category_list,
            'user_list': user_list,
        }
        return HttpResponse(template.render(context, request))
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        product_code = request.POST['product_code']
        user = User.objects.get(id=request.POST['product_owner'])
        category = Category.objects.get(id=request.POST['category'])
        try:
            product = Product.objects.get(product_owner=request.user, id=p_id)
            last_modified = product.modified.date()
            todays_date = datetime.date.today()
            update_time = datetime.time(
                11, 0, 0, 0) > datetime.datetime.now().time()
        
            # product = Product.objects.get(product_owner=request.user, id=p_id)
            if not todays_date == last_modified:
                if update_time:
                    
                        with transaction.atomic():
                            product = Product.objects.get(id=p_id)
                            product.name = name
                            product.price = price
                            product.product_code = product_code
                            product.category = category
                            product.user = user
                            product.save()
                        return JsonResponse(status=200, data={
                            'success': True,
                            'data': 'success',
                            'message': "updated successfully"
                        })
                    
                else:
                    return JsonResponse(status=400, data={
                        'success': False,
                        'data': 'Failed',
                        'message': "You can only update your product before 11 o'clock."
                    })
            else:
                return JsonResponse(status=400, data={
                    'success': False,
                    'data': 'Failed',
                    'message': "You can only update your product once in a day and You have updated it already."
                })
        except Exception as error:
                return JsonResponse(status=400, data={
                'success': False,
                'data': 'Failed',
                'message': "You cant update this product as you are not the owner of this product"
            })
    return HttpResponse(template.render(context, request))


def create_product(request):
    if request.method == 'POST':

        form = ProductForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm(request.GET)
    return render(request, 'create_product.html', {'form': form})


@login_required
def delete(request):
    try:
        Product.objects.get(id=request.POST.get('product_id'),product_owner=request.user,).delete()
        return JsonResponse(status=200, data={
            'success': True,
            'data': 'success',
            'message': "Successfully Deleted"
        })
    except Exception as error:
                return JsonResponse(status=400, data={
                'error': False,
                'data': 'Failed',
                'message': "You cant delete this product as you are not the owner of this product"
            })


@login_required
def category(request):
    template = loader.get_template('category.html')
    if request.method == 'GET':
        category_list = Category.objects.all()
        context = {
            'category_list': category_list,
        }

    if request.method == 'POST':

        type_names = {'name': 'name',
                      'sub_category': 'sub_category',
                      }
        field_type = request.POST.get('type', '')
        field_value = request.POST.get('value', '')
        field_name = request.POST.get('name', '')
        data_dict_update = {field_name: field_value}
        try:
            with transaction.atomic():
                category = Category.objects.get(id=request.POST.get('cat_id'))
                if field_name == 'sub_category':
                    field_value = Category.objects.get(id=field_value)
                category.__setattr__(field_name, field_value)
                category.save()
                return JsonResponse(status=200, data={
                    'success': True,
                    'data': 'success',
                    'message': "updated successfully"
                })
        except Exception as error:
            return JsonResponse(status=400, data={
                'success': False,
                'message': error
            })

    return HttpResponse(template.render(context, request))


def createcategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryForm()
    return render(request, 'createcategory.html', {'form': form})


@login_required
def deletecategory(request):
    try:
        Category.objects.get(id=request.POST.get('cat_id')).delete()
        return JsonResponse(status=200, data={
            'success': True,
            'data': 'success',
            'message': "Successfully Deleted"
        })
    except Exception as error:
        return JsonResponse(status=400, data={
            'success': False,
            'message': error
        })
