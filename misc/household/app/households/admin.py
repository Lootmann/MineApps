from django.contrib import admin
from households.models import HouseHoldModel


@admin.register(HouseHoldModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["category", "cost", "description", "registered_at", "created_at"]
