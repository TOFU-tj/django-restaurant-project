from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from orders.forms import OrderForm


class OrderCreateView(CreateView):
    template_name = "orders/order_create.html"
    form_class = OrderForm

