from django.db import models

from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField

from .constants import CURRENCY_TYPE, CUSTOMER_TYPE, SALUTATION_TYPE

from apps.subscriptions.models import SubscriptionPlan


class Customer(models.Model):
    customer_type = models.CharField(
        max_length=100,
        verbose_name=_("Customer Type"),
        choices=CUSTOMER_TYPE,
        default="INDIVIDUAL",
    )
    salutation = models.CharField(max_length=20, choices=SALUTATION_TYPE)
    company_name = models.CharField(max_length=100, verbose_name=_("Company Name"))
    display_name = models.CharField(max_length=100, verbose_name=_("Display Name"))
    currency = models.CharField(
        max_length=100, verbose_name=_("Currency"), choices=CURRENCY_TYPE
    )
    email = models.EmailField()
    personal_phone = models.CharField(max_length=11, verbose_name=_("Personal Phone"))
    work_phone = models.CharField(max_length=11, verbose_name=_("Work Phone"))
    subscription_plan = models.ForeignKey(
        SubscriptionPlan, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return f"{self.customer_type}"


class CustomerBillingAddress(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    street = models.CharField(max_length=150, verbose_name=_("Street Address"))
    city = models.CharField(max_length=50, verbose_name=_("City"))
    state = models.CharField(max_length=50, verbose_name=_("State"))
    zip_code = models.CharField(max_length=50, verbose_name=_("Zip Code"))
    phone = models.CharField(max_length=11, verbose_name=_("Phone"))
    country = CountryField()

    def __str__(self) -> str:
        return f"{self.customer_type}"


class CustomerShippingAddress(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    street = models.CharField(max_length=150, verbose_name=_("Street Address"))
    city = models.CharField(max_length=50, verbose_name=_("City"))
    state = models.CharField(max_length=50, verbose_name=_("State"))
    zip_code = models.CharField(max_length=50, verbose_name=_("Zip Code"))
    phone = models.CharField(max_length=11, verbose_name=_("Phone"))
    country = CountryField()

    def __str__(self) -> str:
        return f"{self.customer_type}"
