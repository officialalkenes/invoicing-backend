from django.shortcuts import render
from .models import Invoice, Recurring


def recurring_view(request):
    if request.method == "POST":
        invoice_type = request.POST.get("invoice_type")
        if invoice_type == "Recurring":
            recurring_invoices = Recurring.objects.filter(user=request.user)
            return render(
                request, "recurring.html", {"recurring_invoices": recurring_invoices}
            )
    return render(request, "invoice.html")
