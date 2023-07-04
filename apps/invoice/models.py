from django.contrib.auth import get_user_model

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.utils.translation import gettext_lazy as _

from apps.customers.models import Customer
from apps.invoice.constants import BILLING_METHOD, FREQUENCY_CHOICES, INVOICE_TYPE

from .utils import generate_unique_account_number

User = get_user_model()


class Invoice(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_invoice"
    )
    client = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="client_invoice"
    )
    inv_number = models.CharField(max_length=20, blank=True)
    invoice_date = models.DateField(verbose_name=_("Invoice Date"))
    subject = models.CharField(max_length=100, verbose_name=_("Subject"))
    due_date = models.DateField(verbose_name=_("Due Date"), blank=True, null=True)
    invoice_type = models.CharField(
        max_length=20, verbose_name=_("Invoice Type"), choices=INVOICE_TYPE
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=(
            ("draft", "Draft"),
            ("sent", "Sent"),
            ("paid", "Paid"),
            ("cancelled", "Cancelled"),
        ),
        blank=True,
    )
    # ... other invoice fields
    terms = models.TextField(blank=True)
    has_paid = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def __str__(self):
        return self.inv_number

    def save(self, *args, **kwargs):
        if not self.inv_number:
            self.inv_number = generate_unique_account_number()
        return super().save(self, args, kwargs)


@receiver(post_save, sender=Invoice)
def user_post_save(sender, instance, created, **kwargs):
    if instance.has_paid:
        instance.status = "paid"
        instance.save()
    elif instance.is_sent and not instance.has_paid:
        instance.status = "sent"
        instance.save()


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name="item_invoice"
    )
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    total = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    terms = models.TextField(blank=True)

    @property
    def calculate_total(self):
        subtotal = self.quantity * self.unit_price
        if self.discount:
            subtotal -= self.discount
        tax = subtotal * (self.tax_rate / 100)
        self.total = subtotal + tax

    def save(self, *args, **kwargs):
        self.calculate_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description}"


class Recurring(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name=_("user_recurring")
    )
    invoice = models.ForeignKey(
        "Invoice", on_delete=models.CASCADE, related_name=_("invoice_recurring")
    )
    frequency = models.CharField(max_length=2, choices=FREQUENCY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.invoice.number}"


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100, verbose_name=_("Project Name"))
    project_code = models.CharField(max_length=100, verbose_name=_("Project Code"))
    description = models.TextField()
    billing_method = models.CharField(
        max_length=100, verbose_name=_("Billing Method"), choices=BILLING_METHOD
    )
    total_cost = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self) -> str:
        return f"{self.project_name}"


class ProjectTask(models.Model):
    project = models.ManyToManyField(Project)
    task_name = models.CharField(max_length=100, verbose_name=_("Task Name"))
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.task_name}"


class Quote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quote_id = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=100, verbose_name=_("Subject"))
    quote_date = models.DateField(verbose_name=_("Due Date"))
    expiration_date = models.DateField(verbose_name=_("Due Date"))
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, blank=True)
    terms = models.TextField(blank=True, verbose_name=_("Terms and Condition"))
    files = models.FileField(blank=True, upload_to="")
