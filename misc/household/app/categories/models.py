from django.db import models


class CategoryModel(models.Model):
    CATEGORY_TYPES = (
        ("I", "Income"),
        ("E", "Expense"),
        ("D", "Debt"),
        ("O", "Other"),
    )

    name = models.CharField(max_length=255)
    category_type = models.CharField(max_length=1, choices=CATEGORY_TYPES)

    def __str__(self) -> str:
        return f"[{self.category_type}] {self.name}"
