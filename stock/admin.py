from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Product, ProductMessages, ProductType

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ProductMessages)
class ProductMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']