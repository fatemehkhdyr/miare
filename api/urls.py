from django.urls import path, include
from .views import CouriersessionList, DailyIncomeList, WeeklyIncomeList

app_name = "api"

urlpatterns = [
    path("couriersession", CouriersessionList.as_view(), name="couriersession"),
    path("dailyincome", DailyIncomeList.as_view(), name="dailyincome"),
    path('weeklyincome',WeeklyIncomeList.as_view(), name="weeklyincome"),
]