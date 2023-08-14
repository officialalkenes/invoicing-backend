import string
import random


def generate_unique_account_number():
    while True:
        inv_number = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )
        from . import models

        if not models.Invoice.objects.filter(inv_number=inv_number).exists():
            return inv_number
