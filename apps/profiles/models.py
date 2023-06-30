from django.contrib.auth import get_user_model

from django.db import models

from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField

from apps.profiles.utils import generate_unique_id, user_directory_path

from .constants import BUSINESS_TYPE, CURRENCY_CHOICE, INDUSTRY_TYPE


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    organization_name = models.CharField(
        max_length=100, verbose_name=_("Organization Name")
    )
    location = CountryField()
    state = models.CharField(
        max_length=100, verbose_name=_("State/Province"), blank=True
    )
    logo = models.ImageField(
        upload_to=user_directory_path, blank=True, verbose_name=_("Organization Logo")
    )
    city = models.CharField(max_length=100, verbose_name=_("City"), blank=True)
    address = models.CharField(
        max_length=100, blank=True, verbose_name=_("Business Address")
    )
    phone_number = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.user}"


class OrganizationProfile(models.Model):
    org_id = models.CharField(
        primary_key=True, max_length=10, default=generate_unique_id, editable=False
    )
    organization = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    industry = models.CharField(max_length=100, choices=INDUSTRY_TYPE)
    business = models.CharField(max_length=100, choices=BUSINESS_TYPE)
    base_currency = models.CharField(max_length=30, choices=CURRENCY_CHOICE, blank=True)

    def __str__(self) -> str:
        return f"{self.organization}"
