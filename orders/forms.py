from django import forms
from orders.models import Order


class OrderForm(forms.ModelForm): 
    table_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': "form-control",
            'placeholder': "Введите номер стола"
        })
    )

    class Meta: 
        model = Order
        fields = ('table_number',)
