from django.contrib import admin
from typing import Dict, Tuple

from goods.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields: Dict[str, Tuple[str, ...]] = {"slug": ("name",)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields: Dict[str, Tuple[str, ...]] = {"slug": ("name",)}
