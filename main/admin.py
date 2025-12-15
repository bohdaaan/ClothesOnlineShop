from django.contrib import admin
from .models import Product, ProductImage, Category, Size, ProductSize


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductSizeInLine(admin.TabularInline):
    model = ProductSize
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    list_filter = ['name', 'color']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInLine, ProductSizeInLine]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)

