# Bilal ma - Formulaires
from django import forms
from catalogue.models import Order

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method']
