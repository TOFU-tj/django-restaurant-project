from django.urls import path
from orders.views import OrderCreateView, SuccessTemplateView, CanceledTemplateView
from . import views
app_name = 'orders'

urlpatterns = [
    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    path('order-success', SuccessTemplateView.as_view(), name='success'),
    path('order-canceled', CanceledTemplateView.as_view(), name='canceled')
]