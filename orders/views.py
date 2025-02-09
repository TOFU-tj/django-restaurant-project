
from django.shortcuts import render
from django.views import View
from orders.models import Order

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

from orders.forms import OrderForm
from django.urls import reverse_lazy, reverse

from django.http import  HttpResponse
from main.models import Table, Basket




class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = "orders/order_create.html"
    form_class = OrderForm
    success_url = reverse_lazy('orders:success')

    def form_valid(self, form):
        user = self.request.user
        table_number = form.cleaned_data.get("table_number")

        basket_items = Basket.objects.filter(user=user)

        if not basket_items.exists():
            return HttpResponse("Ваша корзина пуста!", status=400)


        basket_history = [
            {
                "product": item.product.name,
                "price": float(item.product.price),
                "quantity": item.quantity,
                "total": float(item.sum())  
            }
            for item in basket_items
        ]

        
        order_total = sum(item["total"] for item in basket_history)
        
        order = Order.objects.create(
            table_number=table_number,
            basket_history=basket_history,
            initiator=user,
            status=Order.WAITING,
            order_total=order_total 
        )


        basket_items.delete()

        return redirect(self.success_url)







class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            queryset = Order.objects.all()
        else:
            queryset = Order.objects.filter(initiator=self.request.user)
        
        status_filter = self.request.GET.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)

        return queryset.order_by('status', '-created')

    def post(self, request, *args, **kwargs):
        order_id = request.POST.get("order_id")
        new_status = request.POST.get("status")
        
       
        try:
            order = Order.objects.get(id=order_id)
            order.status = int(new_status)
            order.save()
        except Order.DoesNotExist:
            pass  
        
        return redirect('orders:order_list')





class OrderDeleteView(UserPassesTestMixin, DeleteView):
    model = Order
    template_name = 'orders/order_confirm_delete.html'  # Шаблон для подтверждения удаления
    success_url = reverse_lazy('orders:order_list')  # После удаления редирект на список заказов

    def test_func(self):
        # Проверяем, является ли пользователь администратором
        return self.request.user.is_superuser or self.request.user.is_staff


    
class SuccessTemplateView(TemplateView): 
    template_name = 'orders/success.html'
    
    
class CanceledTemplateView(TemplateView): 
    template_name = 'orders/canceled.html'
    
    

from django.shortcuts import render
from django.views import View
from orders.models import Order

class RevenueView(View):
    def get(self, request):

        paid_orders = Order.objects.filter(status=Order.PAID)

        total_revenue = sum(order.order_total for order in paid_orders)

        context = {
            'paid_orders': paid_orders,
            'total_revenue': total_revenue,
        }

        return render(request, 'orders/revenue.html', context)

