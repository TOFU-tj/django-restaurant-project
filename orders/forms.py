
from django import forms
from orders.models import Order
from main.models import Table  

class OrderForm(forms.ModelForm):
    table_number = forms.ModelChoiceField(
        queryset=Table.objects.all(),
        empty_label="Выберите стол",
        label="Стол",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Order
        fields = ["table_number"]  # Добавляем table_number в форму
