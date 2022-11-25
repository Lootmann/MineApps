from django.urls import path

from households.views import HouseholdCreateView

app_name = "households"

urlpatterns = [
    path("create/", HouseholdCreateView.as_view(), name="create"),
]
