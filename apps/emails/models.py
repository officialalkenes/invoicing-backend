from django.db import models
from django.contrib.auth.models import User

from apps.invoice.models import Invoice


class Email(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)


class ImportantContent(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    recipient = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)


class EmailTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.ForeignKey(
        "YourEmailModel", on_delete=models.CASCADE
    )  # Replace 'YourEmailModel' with the appropriate email model
    viewed_count = models.PositiveIntegerField(default=0)
