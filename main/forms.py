from django import forms
from .models import Basket, Table

class OrderForm(forms.ModelForm):
    table = forms.ModelChoiceField(queryset=Table.objects.all(), label="Выберите стол")

    class Meta:
        model = Basket
        fields = ["product", "quantity", "table"]