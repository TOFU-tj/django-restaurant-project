from typing import Any
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from main.models import Products, ProductsCategory, Basket, Table 
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView



 
class ProductsListView(ListView):
    model = Products
    template_name = 'main/product_page.html'
    
    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id = category_id) if category_id else queryset
    
    
    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context ["categories"] = ProductsCategory.objects.all() 
        return context
    
    

# def product_page(request, category_id=None):
#     if category_id: 
#         category = ProductsCategory.objects.get(id=category_id)
#         products = Products.objects.filter(category=category)
#     else : 
#         products =  Products.objects.all()
        
#     context = {
#         'categories' : ProductsCategory.objects.order_by('name'),
#         'products' : products
#     }
#     return render(request, 'main/product_page.html', context)





@login_required
def order_page(request):
    baskets = Basket.objects.filter(user=request.user)
    
    order_total = sum(basket.product.price * basket.quantity for basket in baskets)
    order_quantity = sum(basket.quantity for basket in baskets)
    
    context = {
        'baskets': baskets,
        'order_total': order_total,
        'order_quantity': order_quantity,

    }
    return render(request, 'main/order_page.html', context)


@login_required
def order_add(request, product_id):
    product = Products.objects.get(id=product_id)  
    quantity = int(request.POST.get('quantity', 1)) 

    
    baskets = Basket.objects.filter(user=request.user, product=product)
    
    if not baskets.exists():
        # Если корзины нет, создаем новую
        Basket.objects.create(user=request.user, product=product, quantity=quantity)
    else:
        # Если корзина уже существует, обновляем количество товара
        basket = baskets.first()
        basket.quantity += quantity
        basket.save()

    return redirect(request.META.get("HTTP_REFERER", "/"))



@login_required
def basket_remove(request, basket_id):
    if request.method == 'POST': 
        basket = Basket.objects.get(id=basket_id)
        basket.delete() 
        return redirect(request.META.get('HTTP_REFERER', '/'))  
    return redirect('index')



def tracking_page(request): 
    return render(request, 'main/tracking_page.html')