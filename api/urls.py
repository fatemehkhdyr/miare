from django.urls import path, include
from .views import CouriersessionList, DailyIncomeList, WeeklyIncomeList, CouriersList

app_name = "api"

urlpatterns = [
    path("couriers", CouriersList.as_view(), name="couriers"),
    path("couriersession", CouriersessionList.as_view(), name="couriersession"),
    path("dailyincome", DailyIncomeList.as_view(), name="dailyincome"),
    path('weeklyincome',WeeklyIncomeList.as_view(), name="weeklyincome"),
]