from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta

from apps.profiles.models import UserProfile
from apps.subscriptions.constants import OCURRENCE_CHOICES, PAYMENT_METHOD_CHOICES


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Plan Name"))
    price_monthly = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Monthly Price")
    )
    price_yearly = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Yearly Price")
    )
    features = models.TextField(verbose_name=_("Features"))

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    payment_schedule = models.CharField(
        max_length=10,
        choices=OCURRENCE_CHOICES,
        default="monthly",
    )
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHOD_CHOICES,
        default="paypal",
        verbose_name=_("Payment Method"),
    )
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))

    def save(self, *args, **kwargs):
        if self.payment_schedule == "monthly":
            self.start_date = datetime.now().date()
            self.end_date = self.start_date + timedelta(days=30)
        elif self.payment_schedule == "yearly":
            self.start_date = datetime.now().date()
            self.end_date = self.start_date + timedelta(days=365)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.plan} ({self.payment_schedule})"
