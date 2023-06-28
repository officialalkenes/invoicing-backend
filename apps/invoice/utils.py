import string
import random

from . import models


def generate_unique_account_number():
    while True:
        number = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
        if not models.Client.objects.filter(number=number).exists():
            return number
