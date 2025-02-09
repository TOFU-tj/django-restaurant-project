from http import HTTPStatus
from django.views.decorators.csrf import csrf_exempt   

from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

from django.conf import settings
from orders.forms import OrderForm
from django.urls import reverse_lazy, reverse
import stripe
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateView
from main.models import Table, Basket




class OrderCreateView(CreateView):
    template_name = "orders/order_create.html"
    form_class = OrderForm
    success_url = reverse_lazy('orders:success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()  
        return context
        
    def form_valid(self, form):
        form.instance.initiator = self.request.user  
        return super().form_valid(form)


    
class SuccessTemplateView(TemplateView): 
    template_name = 'orders/success.html'
    
    
class CanceledTemplateView(TemplateView): 
    template_name = 'orders/canceled.html'
    
    
