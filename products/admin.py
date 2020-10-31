from django.contrib import admin
from .models import Product, Category

# Register your models here.

admin.site.site_header = "Products Admin"
admin.site.index_title = "Welcome to Products Portal"


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('name','product_code','price','manufacture_date','expiry_date','product_owner','created', 'modified')
    list_filter = ('name','product_code',)
    search_fields = (('name','product_code',))

admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
