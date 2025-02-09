from django.urls import path
from orders.views import OrderCreateView, SuccessTemplateView, CanceledTemplateView, OrderListView, OrderDeleteView, RevenueView

app_name = 'orders'

urlpatterns = [
    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    path("list/", OrderListView.as_view(), name="order_list"),
    path('order-success', SuccessTemplateView.as_view(), name='success'),
    path('order-canceled', CanceledTemplateView.as_view(), name='canceled'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
    path('revenue/', RevenueView.as_view(), name='revenue'),
]