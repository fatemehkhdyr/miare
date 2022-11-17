from rest_framework import serializers
from .models import Couriers, Couriersession, DailyIncome, WeeklyIncome


class Couriersserializer(serializers.ModelSerializer):
    class Meta:
        model = Couriers
        fields = '__all__'

class CouriersessionSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Couriersession
        fields = '__all__'


class DailyIncomeSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = DailyIncome
        fields = '__all__'


class WeeklyIncomeSerialiazer(serializers.ModelSerializer):
    user = Couriersserializer()
    class Meta:
        model = WeeklyIncome
        fields = '__all__'