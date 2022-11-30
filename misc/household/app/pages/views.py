from django.views import generic

from households.models import HouseHoldModel


class PagesIndexView(generic.ListView):
    template_name = "pages/index.html"
    model = HouseHoldModel
    context_object_name = "households"
    ordering = ("-registered_at",)
