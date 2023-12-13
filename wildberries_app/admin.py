from django.contrib import admin
from .models import Category, Param, FilesStorage, Product, Warehouse


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated', 'parent')
    search_fields = ('name',)
    list_filter = ('parent',)
    ordering = ('created',)


@admin.register(Param)
class ParamAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'max_count', 'unit', 'popular', 'required', 'created', 'updated', 'categories')
    search_fields = ('name',)
    list_filter = ('categories',)
    ordering = ('created',)


@admin.register(FilesStorage)
class FilesStorageAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_main', 'size', 'mime_type', 'created', 'updated')
    search_fields = ('name',)
    list_filter = ('is_main',)
    ordering = ('created',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku_wb', 'number_wb', 'sku', 'brand', 'uploaded', 'created', 'updated', 'categories')
    search_fields = ('name', 'sku_wb', 'sku')
    list_filter = ('uploaded', 'categories')
    ordering = ('created',)


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'is_main', 'created', 'updated')
    search_fields = ('name',)
    list_filter = ('is_main',)
    ordering = ('created',)
