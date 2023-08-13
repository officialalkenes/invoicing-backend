from django.urls import path
from .views import CustomerSubscriptionView, SubscriptionPlanListView

urlpatterns = [
    path(
        "customer/<int:customer_id>/subscribe/<int:plan_id>/",
        CustomerSubscriptionView.as_view(),
        name="customer-subscribe",
    ),
    path(
        "subscription-plans/",
        SubscriptionPlanListView.as_view(),
        name="subscription-plans-list",
    ),
    # Other URL patterns
]
