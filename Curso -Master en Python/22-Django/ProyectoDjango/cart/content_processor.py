from .cart import Cart

def cart_total(request):
    total = 0
    if request.session['cart']:
        for key, value in request.session['cart'].items():
            total += float(value['price'])
    print(total)
    return {'total_price': total}

def cart(request):
    return {'cart':Cart(request)}

