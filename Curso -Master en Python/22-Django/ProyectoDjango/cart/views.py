import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from fonluz.models import Article
from .cart import Cart

def created_cart(request):

    return render(request,'cart/created_cart2.html',{'title':'Nuevo pedido'})

"""def cart_add(request, article_id):
    if request.method == 'POST':
        cart = Cart(request)
        article = get_object_or_404(Article, id=article_id)
        quantity = int(request.POST['quantity'])
        cart.add(article,quantity)
        page = request.GET.get('page')
        return redirect(f'/created_cart/?page={page}')"""


@require_POST
def cart_add(request):
    try:
        data = json.loads(request.body)
        article_id = data.get('article_id')
        quantity = int(data.get('quantity'))
        override_quantity = data.get('override_quantity', False)
        cart = Cart(request)
        article = Article.objects.get(id=article_id)
        cart.add(article=article, quantity=quantity, override_quantity=override_quantity)
        return JsonResponse({'status': 'success', 'message': 'Artículo agregado al carrito.'})
    except Article.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El artículo no existe.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

def cart_remove(request, article_id):
    if request.method == 'POST':
        cart = Cart(request)
        article = get_object_or_404(Article, id=article_id)
        cart.remove(article)
        return JsonResponse({'status': 'success', 'message': 'Artículo eliminado del carrito.'})
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {
        'cart':cart
    })

def cart_detail_json(request):
    cart = Cart(request)
    cart_items = []
    for item in cart:
        cart_items.append({
            'id': item['article']['id'],
            'article_name': item['article']['article_name'],
            'quantity': item['quantity'],
            'price': float(item['price']),
            'total_price': float(item['total_price']),
        })
    return JsonResponse({
        'items': cart_items,
        'total_price': float(cart.get_total_price()),
        'total_items': len(cart),
    })

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('/created_cart')
