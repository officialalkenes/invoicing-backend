from datetime import datetime
from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth import get_user_model

from rest_framework import response, views

from apps.invoice.models import Invoice, InvoiceItem, Item, Recurring
from apps.records.serializers import SortedInvoiceRecordSerializer
from apps.records.utils import calculate_date_range


User = get_user_model()


class SortedDepositRecordView(views.APIView):
    # def get(self, request, period, status):
    # Map the period value to time period filters
    # period_filters = {
    #     'daily': {'date__date': 'date'},
    #     'weekly': {'date__week': 'week'},
    #     'monthly': {'date__month': 'month'},
    #     'yearly': {'date__year': 'year'},
    # }
    # filters = period_filters.get(period, {})
    # # Apply the time period and status filters to retrieve the records
    # records = Invoice.objects.filter(**filters, status=status)
    # total_deposit = records.aggregate(total_deposit=Sum('amount'))['total_deposit']

    def get(self, request):
        filter_by = request.GET.get("filter_by")  # Example: Today
        status = request.GET.get("status")  # Example: Completed

        # Convert string dates to datetime objects for comparison
        from_date, to_date = calculate_date_range(filter_by)

        # Filter deposit records based on the provided parameters
        records = Invoice.objects.filter(
            date__range=[from_date, to_date], status=status
        )

        # Serialize the filtered records
        serializer = SortedInvoiceRecordSerializer(records, many=True)
        return response.Response(serializer.data)


filtered_invoices = SortedDepositRecordView.as_view()
