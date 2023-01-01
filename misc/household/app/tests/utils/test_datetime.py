from django.utils import timezone


class TestDatetime:
    def test_get_last_month(self):
        # get the first datetime current month
        this_month = timezone.now().replace(day=1)

        # this month - 1 day = the last day of last month
        last_month = this_month - timezone.timedelta(days=1)

        if this_month.month == 1:
            assert this_month.year == last_month.year + 1 and last_month.month == 12
        else:
            assert this_month.year == last_month.year and this_month.month == last_month.month + 1
