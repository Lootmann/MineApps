from django.urls import reverse_lazy
from django.views import generic

from households.forms import HouseholdsCreateForm, HouseholdUpdateForm
from households.models import HouseHoldModel


class HouseholdCreateView(generic.CreateView):
    template_name = "households/create.html"
    model = HouseHoldModel
    form_class = HouseholdsCreateForm
    success_url = reverse_lazy("pages:index")


class HouseholdUpdateView(generic.UpdateView):
    template_name = "households/update.html"
    model = HouseHoldModel
    form_class = HouseholdUpdateForm

    def get_success_url(self):
        return reverse_lazy("pages:index")
