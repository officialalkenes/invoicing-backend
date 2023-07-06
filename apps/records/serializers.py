from rest_framework import serializers

from django.contrib.auth import get_user_model


from apps.invoice.serializers import InvoiceSerializer


User = get_user_model()


class SortedInvoiceRecordSerializer(serializers.ModelSerializer):
    invoices = InvoiceSerializer(many=True)

    class Meta:
        model = User
        fields = ("invoices",)
