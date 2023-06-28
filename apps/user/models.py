import datetime
import uuid

from django.contrib.auth import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.db import models
from django.db.models.functions import Now
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django_countries.fields import CountryField

# from phonenumber_field.modelfields import PhoneNumberField

from .constants import MEMBER_TYPE
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        verbose_name=_("Email Address"),
        help_text=_("Provide a Valid Email Address"),
    )
    country = CountryField()
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can has teacher's/staff's Priviledges."
        ),
    )
    member_type = models.CharField(
        max_length=100, verbose_name=_("PLATFORM ROLE"), choices=MEMBER_TYPE, blank=True
    )
    is_owner = models.BooleanField(
        default=False,
        verbose_name=_("Owner Validity"),
        help_text=_("Designates whether User is a School Owner"),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    last_login = models.DateTimeField(_("Last Login Date"), auto_now=True)

    verified = models.BooleanField(
        _("email_verify"),
        default=False,
        help_text=_("Designates whether this user's email has been Verified. "),
    )

    on_boarding_complete = models.BooleanField(
        verbose_name=_("Completed Onboarding"),
        default=False,
        help_text=_("Flag to determine if customer has completed onboarding process."),
    )

    on_boarding_complete_date = models.DateTimeField(
        verbose_name=_("Onboarding Complete Date"),
        blank=True,
        null=True,
        help_text=_("Timestamp when customer completed onboarding process."),
    )

    kyc_submitted = models.BooleanField(
        verbose_name=_("KYC Submitted"),
        default=False,
        help_text=_("Flag to determine if customer has submitted a KYC Verification."),
    )

    social_security_number = models.CharField(
        verbose_name=_("Social Security Number"),
        max_length=50,
        blank=True,
        null=True,
        help_text=_(
            "The social security number of the customer. This helps to determine the credit score and also validates the identity of the customer."
        ),
    )

    place_of_birth = models.CharField(
        max_length=150,
        verbose_name=_("Place of Birth"),
        blank=True,
        null=True,
        help_text=_(
            "The place of birth of the customer. This must match the place of birth as indicated in the customers photo Identitication."
        ),
    )

    verification_date = models.DateTimeField(
        default=timezone.now,
        verbose_name=_("Verification Date"),
        blank=True,
        null=True,
        editable=False,
        help_text=_("Timestamp when customers profile was verified."),
    )

    registered_ip_address = models.GenericIPAddressField(
        verbose_name=_("Registered IP Address"),
        blank=True,
        null=True,
        editable=False,
        help_text=_("The IP address recorded at the time of registration."),
    )

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_local_today(self) -> datetime.date:
        """
        Auto Detect Current User's timezone.
        localdate
        """
        return timezone.localdate()

    def __str__(self) -> str:
        return f"{self.email}"

    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, db_index=True, null=True, blank=True)
    login = models.DateTimeField(auto_now_add=True)
    logout = models.DateTimeField(null=True, default=None)


class LoginAttempt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login_attempts = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "user: {}, attempts: {}".format(self.user.email, self.login_attempts)


@receiver(user_logged_in)
def register_login(sender, user, request, **kwargs):
    UserActivity.objects.create(user=user, session_key=request.session.session_key)


@receiver(user_logged_out)
def register_logout(sender, user, request, **kwargs):
    UserActivity.objects.filter(
        user=user, session_key=request.session.session_key
    ).update(logout=Now())


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    return "user {} logged in through page {}".format(
        user.email, request.META.get("HTTP_REFERER")
    )


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    return "user {} logged in failed through page {}".format(
        credentials.get("email"), request.META.get("HTTP_REFERER")
    )


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    return "user {} logged out through page {}".format(
        user.email, request.META.get("HTTP_REFERER")
    )
