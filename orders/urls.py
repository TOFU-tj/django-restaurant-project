from django.urls import path
from orders.views import OrderCreateView
from . import views
app_name = 'orders'

urlpatterns = [
    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    path('sucsess', views.sucsess, name='sucsess')
]