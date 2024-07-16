from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from fonluz.models import Article
from .cart import Cart

def created_cart(request):
    # Obtener articulos
    articles = Article.objects.all()
    # Paginar los articulos aca se pone el parametro de cuantos articulos por pagina
    paginator = Paginator(articles, 3)
    # Obtener numero de pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request,'cart/created_cart.html', {
        'title':'Crear pedido',
        'subtitle':'Seleccion de productos',
        'articles': page_articles
    })

def cart_add(request, article_id):
    if request.method == 'POST':
        cart = Cart(request)
        article = get_object_or_404(Article, id=article_id)
        quantity = int(request.POST['quantity'])
        cart.add(article,quantity)
        page = request.GET.get('page')
        return redirect(f'/created_cart/?page={page}')

def cart_remove(request, article_id):
    cart = Cart(request)
    article = get_object_or_404(Article, id=article_id)
    cart.remove(article)
    return redirect('/created_cart')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {
        'cart':cart
    })

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('/created_cart')
