from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product,Category
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
                                    'placeholder': 'Enter Username',
                                    'class': 'form-control input-area', }), required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
class ProductForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
                                    'placeholder': 'Enter your product name',
                                    'class': 'form-control input-area', }), required=True)
    product_code = forms.CharField(widget=forms.TextInput(attrs={
                                    'placeholder': 'Enter product code',
                                    'class': 'form-control input-area', }), required=True)
    price = forms.CharField(widget=forms.TextInput(attrs={
                                    'placeholder': 'Enter price',
                                    'class': 'form-control input-area', }), required=True)
    class Meta:
        model = Product
        fields = ('name','product_code','price','manufacture_date','expiry_date','category','product_owner')
        widgets = {
        'manufacture_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'expiry_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'category': forms.Select(attrs={'class': 'form-control input-area', }),
        'product_owner': forms.Select(attrs={'class': 'form-control input-area', }),
    }


class CategoryForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
                                    'placeholder': 'Enter your name',
                                    'class': 'form-control input-area', }), required=True)
    class Meta:
        model = Category
        fields = ('name','sub_category')
        widgets = {
        'sub_category': forms.Select(attrs={'class': 'form-control input-area', }),
        }
      