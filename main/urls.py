from django.urls import path 
from . import views
from main.views import ProductsListView

app_name = 'main'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('products/<int:category_id>/', ProductsListView.as_view(), name='product_category'),
    path('order_page/', views.order_page, name='order_page'),
    path('baskets/add/<int:product_id>/', views.order_add, name='order_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
    
]
