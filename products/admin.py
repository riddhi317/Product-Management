from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Category

# Register your models here.

admin.site.site_header = "Products Admin"
admin.site.index_title = "Welcome to Products Portal"


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('name','product_code','price','manufacture_date','expiry_date','category','product_owner','created', 'modified')
    list_filter = ('name','product_code','price','manufacture_date','expiry_date','category','product_owner','created', 'modified')
    search_fields = ('name','product_code','price','manufacture_date','category','expiry_date','product_owner','created', 'modified')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','sub_category',)
    list_filter = ('name','sub_category',)
    search_fields = ('name','sub_category',)

    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
