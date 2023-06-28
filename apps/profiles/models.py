from django.contrib.auth import get_user_model

from django.db import models

from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    organization_name = models.CharField(
        max_length=100, verbose_name=_("Organization Name")
    )
    country = CountryField()
    state = models.CharField(
        max_length=100, verbose_name=_("State/Province"), blank=True
    )
    city = models.CharField(max_length=100, verbose_name=_("City"), blank=True)

    phone_number = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.user}"
