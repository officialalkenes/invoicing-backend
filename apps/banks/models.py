from django.db import models

from django.utils.translation import gettext_lazy as _


class Banks(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Bank Name"))
    bank_code = models.CharField(max_length=100, verbose_name=_("Bank Code"))

    def __str__(self) -> str:
        return f"{self.name} - {self.bank_code}"
