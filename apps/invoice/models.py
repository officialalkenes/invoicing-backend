from django.db import models
from django.contrib.auth import get_user_model

from .utils import generate_unique_account_number

User = get_user_model()


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    # ... other client-related fields

    def __str__(self):
        return self.name


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    number = models.CharField(max_length=20, blank=True)
    date = models.DateField()
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
