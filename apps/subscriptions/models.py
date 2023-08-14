from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.customers.models import Customer
from apps.profiles.models import UserProfile
from apps.subscriptions.constants import OCURRENCE_CHOICES  # Import here


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Plan Name"))
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Price")
    )
    features = models.TextField(verbose_name=_("Features"))
    start_date = models.DateField(verbose_name=_("Start Date"), blank=True)
    end_date = models.DateField(verbose_name=_("End Date"), blank=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    ocurrence = models.CharField(
        max_length=100, verbose_name=_("Occurence"), choices=OCURRENCE_CHOICES
    )
    auto_charge = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.owner} - {self.plan} ({self.start_date} to {self.end_date})"

    def save(self, *args, **kwargs):
        # if self.ocurrence.lower() == "monthly":
        #     start_date
        return super().save(args, kwargs)
