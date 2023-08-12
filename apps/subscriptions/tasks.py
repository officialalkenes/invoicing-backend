# tasks.py
from celery import shared_task
from django.db import transaction
from datetime import datetime, timedelta
from .models import Subscription, SubscriptionPlan

from apps.customers.models import Customer


@shared_task
@transaction.atomic
def create_subscription(customer_id, plan_id):
    customer = Customer.objects.get(id=customer_id)
    plan = SubscriptionPlan.objects.get(id=plan_id)

    # Calculate start and end dates for the subscription
    today = datetime.now().date()
    start_date = today
    end_date = start_date + timedelta(days=30)  # You can adjust the duration

    # Create the subscription
    subscription = Subscription.objects.create(
        customer=customer, plan=plan, start_date=start_date, end_date=end_date
    )

    # Implement PayPal payment processing here
    # ...

    return subscription.id
