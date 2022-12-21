from django.urls import path

from households.views import HouseholdCreateView, HouseholdUpdateView

app_name = "households"

urlpatterns = [
    path("create/", HouseholdCreateView.as_view(), name="create"),
    path("update/<int:pk>/", HouseholdUpdateView.as_view(), name="update"),
]
