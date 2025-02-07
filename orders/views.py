from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

from orders.forms import OrderForm
from django.urls import reverse_lazy

class OrderCreateView(CreateView):
    template_name = "orders/order_create.html"
    form_class = OrderForm
    success_url = reverse_lazy('orders:sucsess') 

    
    def form_valid(self, form):
        form.instance.initiator = self.request.user 
        return super().form_valid(form)
    
    

def sucsess(request): 
    return render (request, 'orders/success.html')