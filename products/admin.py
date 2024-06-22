from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "is_discount",
        "discount_price",
        "detail",
    ]


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = [
        "size",
    ]


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = [
        "color",
    ]
