from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from .models import Customer, CustomerBillingAddress, CustomerShippingAddress
from .serializers import (
    CustomerSerializer,
    CustomerBillingAddressSerializer,
    CustomerShippingAddressSerializer,
)


class CustomerListCreateView(generics.ListCreateAPIView):
    """
    List all customers or create a new customer.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a customer instance.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerBillingAddressCreateView(generics.CreateAPIView):
    """
    Create a new billing address instance.
    """

    serializer_class = CustomerBillingAddressSerializer


class CustomerShippingAddressCreateView(generics.CreateAPIView):
    """
    Create a new shipping address instance.
    """

    serializer_class = CustomerShippingAddressSerializer
