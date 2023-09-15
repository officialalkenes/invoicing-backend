from django.contrib.auth import get_user_model

from django.db import models

from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField

from apps.profiles.utils import generate_unique_id, user_directory_path

from .constants import BUSINESS_TYPE, COLOR_CHOICE, CURRENCY_CHOICE, INDUSTRY_TYPE


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    city = models.CharField(max_length=100, verbose_name=_("City"), blank=True)
    address = models.CharField(
        max_length=100, blank=True, verbose_name=_("Business Address")
    )
    phone_number = models.CharField(max_length=100, blank=True)
    is_onboarded = models.BooleanField(default=False)
    color = models.CharField(
        max_length=200,
        choices=COLOR_CHOICE,
        blank=True,
        verbose_name=_("Customer Preferred Color"),
    )

    def __str__(self) -> str:
        return f"{self.user}"

    def save(self, *args, **kwargs) -> None:
        if not self.color:
            self.color == "Blue"
        self.color = self.color
        return super().save()

    # def create_new_profile_id():
    #     name =
    #     return name


class OrganizationProfile(models.Model):
    org_id = models.CharField(
        primary_key=True, max_length=10, default=generate_unique_id, editable=False
    )
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    organization_name = models.CharField(
        max_length=100, verbose_name=_("Organization Name")
    )
    website = models.CharField(max_length=100)
    industry = models.CharField(max_length=100, choices=INDUSTRY_TYPE)
    business = models.CharField(max_length=100, choices=BUSINESS_TYPE)
    location = CountryField()
    state = models.CharField(
        max_length=100, verbose_name=_("State/Province"), blank=True
    )
    logo = models.ImageField(
        upload_to=user_directory_path, blank=True, verbose_name=_("Organization Logo")
    )
    base_currency = models.CharField(max_length=30, choices=CURRENCY_CHOICE, blank=True)

    def __str__(self) -> str:
        return f"{self.organization}"
