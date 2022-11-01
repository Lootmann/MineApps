import pytest
from pytest_django import asserts
from django.urls import reverse


class TestPagesIndexViews:
    @pytest.fixture(autouse=True)
    def initialize(self, client):
        self.url = reverse("pages:index")
        self.response = client.get(self.url)

    def test_status_code(self):
        assert self.response.status_code == 200

    def test_templates(self):
        asserts.assertTemplateUsed(self.response, "base.html")
        asserts.assertTemplateUsed(self.response, "pages/index.html")

    def test_contains(self):
        asserts.assertContains(self.response, "Hello World")
        asserts.assertContains(self.response, "pages/index.html")
