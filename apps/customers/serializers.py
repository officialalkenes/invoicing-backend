from rest_framework import serializers

from .models import Customer, CustomerBillingAddress, CustomerShippingAddress


class CustomerBillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBillingAddress
        fields = "__all__"


class CustomerShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerShippingAddress
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    billing_address = CustomerBillingAddressSerializer()
    shipping_address = CustomerShippingAddressSerializer()

    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        billing_address_data = validated_data.pop("billing_address")
        shipping_address_data = validated_data.pop("shipping_address")

        billing_address = CustomerBillingAddress.objects.create(**billing_address_data)
        shipping_address = CustomerShippingAddress.objects.create(
            **shipping_address_data
        )

        customer = Customer.objects.create(
            billing_address=billing_address,
            shipping_address=shipping_address,
            **validated_data
        )

        return customer
