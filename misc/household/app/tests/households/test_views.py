import pytest
from django.urls import reverse
from django.utils import timezone
from pytest_django import asserts

from categories.models import CategoryModel
from households.models import HouseHoldModel


@pytest.mark.django_db
class TestHouseHoldsUpdateViewGet:
    @pytest.fixture(autouse=True)
    def initialize(self, client):
        self.category = CategoryModel.objects.create(name="Hospital", category_type="E")
        self.household = HouseHoldModel.objects.create(
            category=self.category, cost=1200, description="Dentist"
        )

        url = reverse("households:update", kwargs={"pk": self.household.id})
        self.response = client.get(url)

    def test_status_code(self):
        assert self.response.status_code == 200

    def test_template_used(self):
        asserts.assertTemplateUsed(self.response, "base.html")
        asserts.assertTemplateUsed(self.response, "households/update.html")

    def test_contains(self):
        asserts.assertContains(self.response, "[Expense] Hospital")
        asserts.assertContains(self.response, "1200")
        asserts.assertContains(self.response, "Dentist")


@pytest.mark.django_db
class TestHouseHoldsUpdateViewPost:
    @pytest.fixture(autouse=True)
    def initialize(self):
        self.category = CategoryModel.objects.create(name="Hospital", category_type="E")
        self.household = HouseHoldModel.objects.create(
            category=self.category, cost=1200, description="Dentist"
        )

    def test_updated(self, client):
        new_category = CategoryModel.objects.create(name="HumanDog", category_type="E")
        current_date = timezone.now()
        url = reverse("households:update", kwargs={"pk": self.household.id})
        data = {
            "category": new_category.id,
            "cost": 99999,
            "description": "Torture",
            "registered_at": current_date,
        }

        response = client.post(url, data)
        asserts.assertRedirects(response, reverse("pages:index"))

        updated = HouseHoldModel.objects.filter(id=self.household.id).first()
        assert updated.category == new_category
        assert updated.cost == 99999
        assert updated.description == "Torture"
        assert updated.registered_at == current_date
