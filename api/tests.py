from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Couriersession, DailyIncome,WeeklyIncome, Couriers
from django.utils import timezone
from freezegun import freeze_time


class ProfileModelTest(TestCase):
    def setUp(self) -> None:
        self.adminuser = get_user_model()(username='test1', email='test1@gmail.com')
        self.adminuser.set_password('t123')
        self.adminuser.is_superuser = True
        self.adminuser.save()
        self.client.force_login(user=self.adminuser)
        self.user1 = Couriers.objects.create(username = 'ali')
        self.user2 = Couriers.objects.create(username = 'sima')

        with freeze_time("2022-11-17"):
            today = timezone.now()
            three_days_ago = today + timezone.timedelta(days=-3)
            five_days_ago = today+timezone.timedelta(days=-5)
            eight_days_ago = timezone.now()+timezone.timedelta(days=-8)
            ten_days_ago = timezone.now()+timezone.timedelta(days=-10)
            self.couriersession1 = Couriersession.objects.create(user = self.user1, revenue_type = "s", amount = 10000, courier_time = today)
            self.couriersession2 = Couriersession.objects.create(user = self.user1, revenue_type = "s", amount = 30000, courier_time = today)
            self.couriersession3 = Couriersession.objects.create(user = self.user1, revenue_type = "s", amount = 50000, courier_time = three_days_ago)
            self.couriersession4 = Couriersession.objects.create(user = self.user1, revenue_type = "s", amount = 40000, courier_time = five_days_ago)
            self.couriersession5 = Couriersession.objects.create(user = self.user1, revenue_type = "s", amount = 60000, courier_time = eight_days_ago)
            self.couriersession6 = Couriersession.objects.create(user = self.user1, revenue_type = "s", amount = 70000, courier_time = ten_days_ago)

        with freeze_time("2022-11-17"):
            today = timezone.now()
            three_days_ago = today + timezone.timedelta(days=-3)
            five_days_ago = today+timezone.timedelta(days=-5)
            eight_days_ago = timezone.now()+timezone.timedelta(days=-8)
            ten_days_ago = timezone.now()+timezone.timedelta(days=-10)
            self.couriersession1 = Couriersession.objects.create(user = self.user2, revenue_type = "s", amount = 10000, courier_time = today)
            self.couriersession2 = Couriersession.objects.create(user = self.user2, revenue_type = "s", amount = 20000, courier_time = today)
            self.couriersession3 = Couriersession.objects.create(user = self.user2, revenue_type = "s", amount = 25000, courier_time = today)
            self.couriersession4 = Couriersession.objects.create(user = self.user2, revenue_type = "s", amount = 40000, courier_time = three_days_ago)
            self.couriersession5 = Couriersession.objects.create(user = self.user2, revenue_type = "s", amount = 60000, courier_time = three_days_ago)
            self.couriersession6 = Couriersession.objects.create(user = self.user2, revenue_type = "s", amount = 10000, courier_time = eight_days_ago)
            self.couriersession7 = Couriersession.objects.create(user = self.user2, revenue_type = "s", amount = 20000, courier_time = ten_days_ago)

    def test_when_calculte_user1_daily_income_Expect_value_is_equal_mylist(self):
        response = self.client.get(reverse('api:dailyincome'))
        amounts = []
        for element in response.json():
            if element['user']== self.user1.pk:
                amounts.append(element['amount'])
        self.assertEqual(amounts, [40000,50000,40000,60000,70000])

    def test_when_calculte_user1_weekly_income_Expect_value_is_equal_mylist(self):
        self.client.get(reverse('api:dailyincome'))
        response = self.client.get(reverse('api:weeklyincome'), {"from_date":"2022-11-01", "to_date":"2022-11-20"})
        amounts = []
        for element in response.json():
            if element['user']['id']== self.user1.pk:
                amounts.append(element['amount'])
        self.assertEqual(amounts, [130000,130000])

    def test_when_calculte_user2_daily_income_Expect_value_is_equal_mylist(self):
        response = self.client.get(reverse('api:dailyincome'))
        amounts = []
        for element in response.json():
            if element['user']==self.user2.pk:
                amounts.append(element['amount'])
        self.assertEqual(amounts, [55000,100000,10000,20000])

    def test_when_calculte_user2_weekly_income_Expect_value_is_equal_mylist(self):
        self.client.get(reverse('api:dailyincome'))
        response = self.client.get(reverse('api:weeklyincome'), {"from_date":"2022-11-01", "to_date":"2022-11-20"})
        amounts = []
        for element in response.json():
            if element['user']['id']==self.user2.pk:
                amounts.append(element['amount'])
        self.assertEqual(amounts, [155000,30000])
