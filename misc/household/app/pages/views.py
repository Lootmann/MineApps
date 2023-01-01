from django.db.models import Sum
from django.utils import timezone
from django.views import generic

from households.models import HouseHoldModel


def get_aggregate_households(year: int, month: int):
    aggregations = (
        HouseHoldModel.objects.filter(registered_at__year=year, registered_at__month=month)
        .values("category__name")
        .annotate(total_cost=Sum("cost"))
        .order_by("category__name")
    )

    return aggregations


class PagesIndexView(generic.ListView):
    template_name = "pages/index.html"
    model = HouseHoldModel
    context_object_name = "households"
    ordering = ("-registered_at",)
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["household_aggregates"] = (
            HouseHoldModel.objects.values("category__name")
            .annotate(total_cost=Sum("cost"))
            .order_by("category__name")
        )

        # get two months ago, last month and this month aggregations
        this_month = timezone.now()
        last_month = this_month.replace(day=1) - timezone.timedelta(days=1)
        two_month_ago = last_month.replace(day=1) - timezone.timedelta(days=1)

        context["this_month"] = get_aggregate_households(
            year=this_month.year, month=this_month.month
        )

        context["last_month"] = get_aggregate_households(
            year=last_month.year, month=last_month.month
        )

        context["two_month"] = get_aggregate_households(
            year=two_month_ago.year, month=two_month_ago.month
        )

        return context
