from django import forms

from .models import Invoice, InvoiceItem, Recurring


class InvoiceForm(forms.ModelForm):
    invoice_type = forms.ChoiceField(
        choices=(("Once", "Once"), ("Recurring", "Recurring")), widget=forms.RadioSelect
    )

    class Meta:
        model = Invoice
        fields = "__all__"


class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = "__all__"


class RecurringForm(forms.ModelForm):
    class Meta:
        model = Recurring
        fields = "__all__"


# Pending Htmx Implementation

# class InvoiceForm(forms.ModelForm):
#     invoice_type = forms.ChoiceField(
#         choices=(('Once', 'Once'), ('Recurring', 'Recurring')),
#         widget=forms.RadioSelect,
#         initial='Once',
#         label='Invoice Type',
#         required=True
#     )
#     recurring_field = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'hidden'}),
#         required=False
#     )

#     class Meta:
#         model = Invoice
#         fields = "__all__"

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['recurring_field'].widget.attrs['hx-trigger'] = 'change'
#         self.fields['recurring_field'].widget.attrs['hx-get'] = '/recurring-form/'
#         self.fields['recurring_field'].widget.attrs['hx-target'] = '#recurring-form-wrapper'
#         self.fields['recurring_field'].widget.attrs['hx-swap'] = 'outerHTML'
