from django.db import models
from django.utils import timezone

from categories.models import CategoryModel


class HouseHoldModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    cost = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    registered_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return str(self.category)
