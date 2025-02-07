from django.urls import path 
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.product_page, name='product_page'),
    path('products/<int:category_id>/', views.product_page, name='product_category'),
    path('order_tracking_page', views.tracking_page, name='tracking_page'),
    path('order_page/', views.order_page, name='order_page'),
    path('baskets/add/<int:product_id>/', views.order_add, name='order_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
    # path('set_table/<int:basket_id>/', views.set_table, name='set_table'),

]
