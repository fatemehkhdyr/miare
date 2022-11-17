from django.db import models
from django.db import transaction


class Couriers(models.Model):
    username = models.CharField(max_length=100, unique=True)
    def __str__(self) -> str:
        return self.username


class Couriersession(models.Model):
    REVENUE_TYPE_CHOICES = (
    ("s","salary"),
    ("p", "prize"),
    ("f", "fine"),
    )
    user = models.ForeignKey(Couriers, on_delete=models.CASCADE)
    revenue_type = models.CharField(max_length=20, choices=REVENUE_TYPE_CHOICES)
    amount = models.IntegerField()
    courier_time = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.user.username) + str(self.pk)


class DailyIncome(models.Model):
    user = models.ForeignKey(Couriers, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()

    def __str__(self) -> str:
        return "{} ({}-{})".format(str(self.user.username), str(self.date.month), str(self.date.day))


class WeeklyIncome(models.Model):
    user = models.ForeignKey(Couriers, on_delete=models.CASCADE)
    week_sat = models.DateField()
    amount = models.IntegerField()

    def __str__(self) -> str:
        return "{} ({}-{})".format(str(self.user.username), str(self.week_sat.month), str(self.week_sat.day))

