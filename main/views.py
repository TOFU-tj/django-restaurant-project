from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from main.models import Products, ProductsCategory, Basket, Table 
from django.http import HttpResponseRedirect
from django.contrib import messages


def product_page(request, category_id=None):
    if category_id: 
        category = ProductsCategory.objects.get(id=category_id)
        products = Products.objects.filter(category=category)
    else : 
        products =  Products.objects.all()
        
    context = {
        'tables' : Table.objects.all(),
        'categories' : ProductsCategory.objects.order_by('name'),
        'products' : products
    }
    return render(request, 'main/product_page.html', context)



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
    product = get_object_or_404(Products, id=product_id)  # Получаем продукт
    quantity = int(request.POST.get('quantity', 1))  # Получаем количество из формы, по умолчанию 1

    
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
        basket = get_object_or_404(Basket, id=basket_id)
        basket.delete()  # Удаляем корзину
        return redirect(request.META.get('HTTP_REFERER', '/'))  # Перенаправляем обратно на предыдущую страницу
    return redirect('index')



def tracking_page(request): 
    return render(request, 'main/tracking_page.html')