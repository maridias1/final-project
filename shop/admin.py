from django.contrib import admin
from .models import Product

# ვარეგისტრირებთ Product-ს, რომ გამოჩნდეს /admin/ პანელში
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'brand', 'stock', 'rating')