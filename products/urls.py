"""Product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, url
    2. Add a URL to urlpatterns: url('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url

from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    url(r'^$', views.signup, name='signup'),
    url(r'^home/$', views.home, name='home'),
    url(r'^product/$', views.product, name='product'),
    url(r'^update_product/(?P<p_id>\d+)/$', views.update_product, name='update_product'),
    url(r'^category/$', views.category, name='category'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', LogoutView.as_view(),  name='logout'),

    # # url('', views.index, name='index'),
    url(r'^create_product/$', views.create_product, name='create_product'), 
    url(r'^delete/$', views.delete, name='delete'),   
    url(r'^createcategory/$', views.createcategory, name='createcategory'),
    url(r'^deletecategory/$', views.deletecategory, name='deletecategory'),
    
]