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

    class Meta:
        ordering = ["category_type"]

    def get_category_type_fullname(self, category_type: str) -> str:
        for category in self.CATEGORY_TYPES:
            if category[0] == category_type:
                return category[1]
        raise ValueError("unknown category_type")

    def __str__(self) -> str:
        return f"[{self.get_category_type_fullname(self.category_type)}] {self.name}"
