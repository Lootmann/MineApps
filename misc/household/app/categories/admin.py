from django.contrib import admin
from categories.models import CategoryModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name", "category_type"]
