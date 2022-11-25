from django.urls import reverse_lazy
from django.views import generic

from households.forms import HouseholdsCreateForm
from households.models import HouseHoldModel


class HouseholdCreateView(generic.CreateView):
    template_name = "households/create.html"
    model = HouseHoldModel
    form_class = HouseholdsCreateForm
    success_url = reverse_lazy("pages:index")
