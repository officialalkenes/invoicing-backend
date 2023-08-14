import requests
from django.conf import settings


url = "https://api.paystack.co/bank"
headers = {"Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    banks = response.json().get("data", [])
    for bank in banks:
        bank_name = bank.get("name")
        bank_slug = bank.get("slug")
        bank_code = bank.get("code")
        print(f"Bank Name: {bank_name}, Bank Code: {bank_code}")
else:
    print("Failed to fetch banks:", response.text)
