from django.contrib import admin
from unfold.admin import ModelAdmin

from shop.models import Category, Product


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = (
        "title",
        "description",
        "attachment",
        "parent_id",
        "app",
        "is_deleted",
    )
    fields = (
        "title",
        "description",
        "attachment",
        "parent",
        "app",
    )
    search_fields = (
        "title",
        "description",
        "app",
        "parent",
        "id",
    )

    list_filter_submit = True


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = (
        "title",
        "description",
        "category",
        "parent_id",
        "app",
        "is_deleted",
    )
    fields = (
        "title",
        "description",
        "attachment",
        "parent",
        "category",
        "price",
        "discount_percentage",
        "rating",
        "stock",
        "app",
    )
    search_fields = (
        "title",
        "description",
        "app",
        "parent",
        "category",
        "id",
    )

    list_filter_submit = True
