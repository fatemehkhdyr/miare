from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Couriersession, DailyIncome,WeeklyIncome, Couriers
from django.utils import timezone


class ProfileModelTest(TestCase):
    def setUp(self) -> None:
        self.adminuser = get_user_model()(username='test1', email='test1@gmail.com')
        self.adminuser.set_password('t123')
        self.adminuser.is_superuser = True
        self.adminuser.save()
        self.client.force_login(user=self.adminuser)
        self.user1 = Couriers.objects.create(username = 'ali')
        self.user2 = Couriers.objects.create(username = 'sima')
        three_days_ago = timezone.now()+timezone.timedelta(days=-3)
        eight_days_ago = timezone.now()+timezone.timedelta(days=-8)
        self.couriersession1 = Couriersession.objects.create(user = self.user1, revenue_type = "s", amount = 10000, courier_time = timezone.now())
        self.couriersession3 = Couriersession.objects.create(user = self.user1, revenue_type = "s", amount = 30000, courier_time = three_days_ago)
        self.couriersession4 = Couriersession.objects.create(user = self.user1, revenue_type = "s", amount = 50000, courier_time = eight_days_ago)

    def test_when_calculte_user1_daily_income_Expect_value_is_equal_mylist(self):
        response = self.client.get(reverse('api:dailyincome'))
        amounts = []
        for element in response.json():
            amounts.append(element['amount'])
        self.assertEqual(amounts, [10000, 30000, 50000])

    def test_when_calculte_user1_weekly_income_Expect_value_is_equal_mylist(self):
        self.client.get(reverse('api:dailyincome'))
        response = self.client.get(reverse('api:weeklyincome'), {"from_date":"2022-11-01", "to_date":"2022-11-18"})
        amounts = []
        for element in response.json():
            amounts.append(element['amount'])
        self.assertEqual(amounts, [40000, 50000])
