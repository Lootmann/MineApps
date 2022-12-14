from django import forms

from pages.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ("title", "file")
