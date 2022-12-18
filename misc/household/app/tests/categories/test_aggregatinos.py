import pytest

# from pytest_django import asserts
from django.db.models import Sum

from categories.models import CategoryModel
from households.models import HouseHoldModel


@pytest.mark.django_db
class TestCategoryModelAggregate:
    @pytest.fixture(autouse=True)
    def initial(self, client):
        # create CategoryModels
        grocery = CategoryModel.objects.create(name="Grocery", category_type="E")
        tobacco = CategoryModel.objects.create(name="Tobacco", category_type="E")

        # create HouseholdModels
        HouseHoldModel.objects.create(category=grocery, cost=500)
        HouseHoldModel.objects.create(category=grocery, cost=2500)
        for _ in range(8):
            HouseHoldModel.objects.create(category=grocery, cost=1200)

        for _ in range(10):
            HouseHoldModel.objects.create(category=tobacco, cost=1000)

        self.grocery_sum = 500 + 2500 + 1200 * 8
        self.tobacco_sum = 10 * 1000

    def test_models_are_created(self):
        assert CategoryModel.objects.count() == 2
        assert HouseHoldModel.objects.count() == 20

    def test_values(self):
        households = HouseHoldModel.objects.values("category__name").annotate(Sum("cost"))
        assert len(households) == 2

        assert households[0]["cost__sum"] == self.grocery_sum
        assert households[1]["cost__sum"] == self.tobacco_sum

    def test_filter_and_annotate(self):
        household_filter_by_category = HouseHoldModel.objects.filter(category__name="Grocery")
        household_category_sum = household_filter_by_category.aggregate(Sum("cost"))
        assert household_category_sum["cost__sum"] == 12600
