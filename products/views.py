from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm,ProductForm

from django.http import HttpResponse
from django.template import loader

from .models import Product,Category
from django.db import transaction
from django.http import JsonResponse



@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':

        # form = SignUpForm(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return render(request, 'home.html');
            # return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def login(request):
    if request.method == 'POST': 
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            form = auth_login(request, user) 
            print('user logged in')
            return render(request, 'home.html');
        else: 
            print('Account does not exists. Please try to sign in again');

    form = AuthenticationForm() 
    return render(request, 'login.html', {'form':form, 'title':'log in'})


@login_required
def product(request):
    template = loader.get_template('index.html')
    if request.method=='GET':
        product_list = Product.objects.all()
        # import pdb; pdb.set_trace()
        category_list = Category.objects.all()
        form = ProductForm()
        context = {
            'product_list': product_list,
            'category_list': category_list,
            'form': form
        }

    if request.method=='POST':
        
        type_names = {'name': 'name',
                      'product_code':'product_code',
                      'price':'price',
                      'category': 'category',
                      'manufacture_date': 'expiry_date',
                      'product_owner': 'product_owner',
                      }
        field_type = request.POST.get('type', '')
        field_value = request.POST.get('value', '')
        field_name = request.POST.get('name', '')        
        data_dict_update = {field_name: field_value}
        
        try:

            with transaction.atomic():
                product=Product.objects.get(id =request.POST.get('product_id'))
                if field_name == 'category':
                    field_value = Category.objects.get(id=field_value)
                product.__setattr__(field_name, field_value)
                product.save()
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

def createproduct(request):
    if request.method == 'POST':

        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html');
            # return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'index.html', {'form': form})
  
@login_required
def delete(request):
    product_list = Product.objects.all()
    template = loader.get_template('index.html')
    context = {
        'product_list': product_list,
    }
    return HttpResponse(template.render(context, request))