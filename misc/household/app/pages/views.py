from django.db.models import Sum
from django.views import generic

from households.models import HouseHoldModel


class PagesIndexView(generic.ListView):
    template_name = "pages/index.html"
    model = HouseHoldModel
    context_object_name = "households"
    ordering = ("-registered_at",)
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["household_aggregates"] = HouseHoldModel.objects.values("category__name").annotate(
            total_cost=Sum("cost")
        )
        return context
