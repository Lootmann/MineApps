from django import forms

from households.models import HouseHoldModel


class DatetimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d %H:%M"
        super().__init__(**kwargs)


class HouseholdsCreateForm(forms.ModelForm):
    class Meta:
        model = HouseHoldModel
        fields = ("category", "cost", "description", "registered_at")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["registered_at"].widget = DatetimeLocalInput()
