from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Couriersession, DailyIncome,WeeklyIncome
from .utils import calculate_sat


@receiver(post_save, sender=Couriersession)
def calculate_courirs_daily_income(sender, instance, created, **kwargs):
    if created:
        try:
            daily_income = DailyIncome.objects.get(user = instance.user, date = instance.courier_time)
        except DailyIncome.DoesNotExist:
            daily_income = None
        if not daily_income:
            DailyIncome.objects.create(user = instance.user, amount = instance.amount, date = instance.courier_time)
            return
        new_amount = instance.amount + daily_income.amount
        DailyIncome.objects.filter(user = instance.user, date = instance.courier_time).update(amount = new_amount)
        # update weeklyincome
        week_sat = calculate_sat(daily_income.date)
        try:
            weekly_income = WeeklyIncome.objects.get(user = instance.user, week_sat = week_sat)
        except WeeklyIncome.DoesNotExist:
            weekly_income = None
        if weekly_income:
            new_weekly_amount = weekly_income.amount + instance.amount
            WeeklyIncome.objects.filter(user = instance.user, week_sat = week_sat).update(amount = new_weekly_amount)



@receiver(post_save, sender=DailyIncome)
def calculate_courirs_weekly_income(sender, instance, created, **kwargs):
    if created:
        pass
        week_sat = calculate_sat(instance.date)
        try:
            weekly_income = WeeklyIncome.objects.get(user = instance.user, week_sat = week_sat)
        except WeeklyIncome.DoesNotExist:
            weekly_income = None
        if not weekly_income:
            WeeklyIncome.objects.create(user = instance.user, amount = instance.amount, week_sat = week_sat)
            return
        new_amount = instance.amount + weekly_income.amount
        WeeklyIncome.objects.filter(user = instance.user, week_sat = week_sat).update(amount = new_amount)

        
        
        