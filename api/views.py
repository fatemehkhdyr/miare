from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import permissions
from .models import Couriersession, DailyIncome, WeeklyIncome, Couriers
from .serializer import CouriersessionSerialiazer,DailyIncomeSerialiazer, WeeklyIncomeSerialiazer, Couriersserializer


class CouriersList(ListCreateAPIView):
    queryset = Couriers.objects.all()
    serializer_class = Couriersserializer
    permission_classes = [permissions.IsAdminUser]

class CouriersessionList(ListCreateAPIView):
    queryset = Couriersession.objects.all()
    serializer_class = CouriersessionSerialiazer
    permission_classes = [permissions.IsAdminUser]

class DailyIncomeList(ListAPIView):
    queryset = DailyIncome.objects.all()
    serializer_class = DailyIncomeSerialiazer

class WeeklyIncomeList(ListAPIView):
    serializer_class = WeeklyIncomeSerialiazer
    def get_queryset(self):
        from_date = self.request.query_params.get("from_date")
        to_date = self.request.query_params.get("to_date")
        queryset = WeeklyIncome.objects.filter(week_sat__gte = from_date, week_sat__lte = to_date)
        return queryset
