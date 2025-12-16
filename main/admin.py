from django.contrib import admin
from .models import Product, ProductImage, Category, Size, ProductSize


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductSizeInLine(admin.TabularInline):
    model = ProductSize
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    list_filter = ['name', 'color']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInLine, ProductSizeInLine]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']



