from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="", blank=True)

    def __str__(self) -> str:
        return self.title
