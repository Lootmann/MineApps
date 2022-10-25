from django.urls import reverse_lazy
from django.views import generic

from pages.forms import DocumentForm
from pages.models import Document


class PagesIndexView(generic.CreateView):
    template_name = "pages/index.html"
    model = Document
    form_class = DocumentForm
    context_object_name = "document"
    success_url = reverse_lazy("pages:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["files"] = Document.objects.all()
        return context
