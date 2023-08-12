from django.urls import path
from . import views

app_name = "customers"

urlpatterns = [
    path(
        "customers/",
        views.CustomerListCreateView.as_view(),
        name="customer-list-create",
    ),
    path(
        "customers/<int:pk>/",
        views.CustomerRetrieveUpdateDestroyView.as_view(),
        name="customer-retrieve-update-destroy",
    ),
    path(
        "billing-address/",
        views.CustomerBillingAddressCreateView.as_view(),
        name="billing-address-create",
    ),
    path(
        "shipping-address/",
        views.CustomerShippingAddressCreateView.as_view(),
        name="shipping-address-create",
    ),
]
