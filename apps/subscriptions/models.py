from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.customers.models import Customer


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Plan Name"))
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Price")
    )
    features = models.TextField(verbose_name=_("Features"))

    def __str__(self):
        return self.name


class Subscription(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))

    def __str__(self):
        return f"{self.customer} - {self.plan} ({self.start_date} to {self.end_date})"
