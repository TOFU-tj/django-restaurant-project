from main.models import Basket

def basket(request):
    user = request.user

    baskets = Basket.objects.filter(user=user) if user.is_authenticated else []

    order_total = sum(basket.product.price * basket.quantity for basket in baskets)
    
    return {
        'basket': baskets,  
        'order_total': order_total,  
    }
