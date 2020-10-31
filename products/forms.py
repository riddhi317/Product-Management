from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product,Category


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class ProductForm(forms.Form):
    name = forms.CharField(max_length=30)
    product_code = forms.CharField(max_length=30)
    price = forms.FloatField()
    # category = forms.ForeignKey("Category", verbose_name=_(u"Category"),blank=True,null=True,related_name="+", on_delete=forms.CASCADE)
    manufacture_date = forms.DateField(widget = forms.SelectDateWidget)
    expiry_date = forms.DateField(widget = forms.SelectDateWidget)
    product_owner = forms.CharField(max_length=30)
    class Meta:
        model = Product
        fields = ('name','product_code','price','manufacture_date','expiry_date','product_owner','category')
