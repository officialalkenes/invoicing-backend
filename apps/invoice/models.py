from django.db import models
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _

from apps.customers.models import Customer
from apps.invoice.constants import FREQUENCY_CHOICES, INVOICE_TYPE

from .utils import generate_unique_account_number

User = get_user_model()


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    number = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=100, verbose_name=_("Subject"))
    due_date = models.DateField(verbose_name=_("Due Date"))
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
    )
    payment_due_date = models.DateField(null=True, blank=True)
    # ... other invoice fields
    terms = models.TextField(blank=True)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        if not self.number:
            self.number = generate_unique_account_number()
        return super().save(self, args, kwargs)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items")
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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice = models.ForeignKey("Invoice", on_delete=models.CASCADE)
    frequency = models.CharField(max_length=2, choices=FREQUENCY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.invoice.number}"
