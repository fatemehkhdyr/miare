from django.contrib import admin
from .models import Couriers, Couriersession, DailyIncome, WeeklyIncome


class Couriersadmin(admin.ModelAdmin):
    pass

admin.site.register(Couriers, Couriersadmin)


class Couriersessionadmin(admin.ModelAdmin):
    pass

admin.site.register(Couriersession, Couriersessionadmin)


class DailyIncomeadmin(admin.ModelAdmin):
    pass

admin.site.register(DailyIncome, DailyIncomeadmin)


class WeeklyIncomeadmin(admin.ModelAdmin):
    pass

admin.site.register(WeeklyIncome, WeeklyIncomeadmin)
