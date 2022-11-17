from rest_framework.generics import ListCreateAPIView, ListAPIView
from .models import Couriersession, DailyIncome, WeeklyIncome
from .serializer import CouriersessionSerialiazer,DailyIncomeSerialiazer, WeeklyIncomeSerialiazer


class CouriersessionList(ListCreateAPIView):
    queryset = Couriersession.objects.all()
    serializer_class = CouriersessionSerialiazer

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
