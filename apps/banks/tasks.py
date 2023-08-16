import requests
from django.conf import settings
from celery import shared_task
from .models import Banks


@shared_task
def fetch_and_store_banks():
    url = "https://api.paystack.co/bank"
    headers = {"Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        banks = response.json().get("data", [])
        for bank in banks:
            bank_name = bank.get("name")
            bank_code = bank.get("code")
            Banks.objects.update_or_create(
                bank_code=bank_code, defaults={"name": bank_name}
            )
        print("Banks updated successfully.")
    else:
        print("Failed to fetch banks:", response.text)
