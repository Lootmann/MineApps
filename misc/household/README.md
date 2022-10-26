# Household

## Models

### Household

```python
import timezone

from django.db import models


class Category(models.Model):
  CATEGORY_TYPES = (
    ("I", "Income"),
    ("E", "Expense"),
    ("D", "Debt"),
    ("O", "Other"),
  )
  name = models.CharField(max_length=255)
  category_type = models.TextChoices(max_length=1, choices=CATEGORY_TYPES)


class Household:
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  cost = models.PositiveInteger(default=0)
  description = models.TextField()

  registered_at = models.DateTimeField(default=timezone.now)
  created_at = models.DateTimeField(auto_now_add=True)
  # updated_at = models.DateTimeField(auto_add=True) # don't need ?
```
