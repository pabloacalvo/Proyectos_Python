from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import OrderItem, OrderStatus, Order
from .forms import OrderCreateForm, OrderItemsForm, OrderItemsFormSet
from cart.cart import Cart
from decimal import Decimal
from fonluz.models import Article
from datetime import date
from fonluz.models import ArticleParts


def createOrder(request):
    # Obtenemos la session del carrito
    cart = Cart(request)
    # Si se envia el formulario
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # Obtener el cliente seleccionado en el form y el estado default
            data_form = form.cleaned_data
            client = data_form['client']
            discount = data_form['discount']
            default_status = OrderStatus.objects.get(pk=1)

            # Crear la orden asociada al cliente
            order = form.save(commit=False)
            order.client = client
            order.status = default_status
            order.discount = discount
            if order.discount > 0:
                total_partial = cart.get_total_price()
                # Parseamos el descuento a 0,***
                discount = discount / Decimal(100)
                # Obtenemos el valor del descuento
                total_discount = Decimal(order.total) * discount
                order.total = total_partial - total_discount
            else:
                order.total = cart.get_total_price()
            order.save()

            for article in cart:
                # Reconvertir JSON a objeto Article
                article_instance = Article.objects.get(id=article['article']['id'])
                OrderItem.objects.create(
                    order=order,
                    article=article_instance,  # Utiliza el objeto Article reconvertido
                    price=article['price'],
                    quantity=article['quantity']
                )
            cart.clear()
            return redirect('orders:get_orders')
    # Se pide el form
    else:
        form = OrderCreateForm()
    return render(request,'orders/create_order.html',
                  {
                      'title': 'Nuevo pedido',
                      'cart': cart,
                      'form': form
                  })


def getOrders(request):
    return render(request, 'orders/order_view2.html',{'title':'Gestion de pedidos'})

def orderList(request):
    data = []
    orders = Order.objects.all()
    for order in orders:
        # Filtramos pedidos que no esten "Entregados"
        if order.status.id != 2:
            data.append(order.toJSON())

    # Parametro safe=false porque JsonResponse espera un objeto dict y le estoy pasando una lista de dict
    return JsonResponse(data,safe=False)

def getAllOrders(request):
    data = []
    orders = Order.objects.all()
    for order in orders:
        data.append(order.toJSON())

    return JsonResponse(data,safe=False)

def getOrderItems(request, order_id):
    # Obtener el pedido
    order = get_object_or_404(Order, id=order_id)
    # Obtener todos los artículos del pedido
    order_items = OrderItem.objects.filter(order=order)

    return render(request, 'orders/order_modalDetails.html', {
        'order': order,
        'order_items': order_items
    })

def deleteOrder(request,order_id):
    order = get_object_or_404(Order, id=order_id)

    order.delete()

    return redirect('orders:get_orders')



def editOrder(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST, instance=order)
        formset = OrderItemsFormSet(request.POST, instance=order)

        if order_form.is_valid() and formset.is_valid():
            # Guardar la orden principal sin commit para realizar modificaciones
            order = order_form.save(commit=False)

            # Guardar el formset de OrderItems
            instances = formset.save(commit=False)
            for instance in instances:
                instance.order = order
                instance.save()

            # Calcular el total de los items del pedido
            update_total = Decimal(0)
            for form in formset.forms:
                if form.cleaned_data:
                    quantity = form.cleaned_data['quantity']
                    price = form.cleaned_data['price']
                    total_item = quantity * price
                    update_total += total_item

            # Aplicar descuento si es necesario
            discount = order_form.cleaned_data.get('discount', Decimal(0))
            if discount > 0:
                total_partial = update_total
                discount_percentage = discount / Decimal(100)
                total_discount = total_partial * discount_percentage
                order.total = total_partial - total_discount
            else:
                order.total = update_total

            # Guardar la orden actualizada
            order.save()

            return redirect('orders:get_orders')
        else:
            return redirect('orders:get_orders')
    else:
        order_form = OrderCreateForm(instance=order)
        formset = OrderItemsFormSet(instance=order)

    return render(request, 'orders/order_modalDetails.html', {
        'form': order_form,
        'formset': formset,
        'order_id': order_id
    })

# Metodo para entregar la orden y descontar stock
def deliverOrder(request, order_id):
    try:
        order = get_object_or_404(Order, id=order_id)
        delivered_status = OrderStatus.objects.get(pk=2)
        if delivered_status.id == order.status.id:
            return JsonResponse({'status': 'no-change', 'message': 'success'})
        else:
            # Obtengo los articulos de la orden
            order_items = order.get_order_items()
            # Descontar stock de articulos y sus partes
            for item in order_items:
                item.article.reduce_stock(item.quantity)
                # Obtengo las ArticleParts del articulo entregado
                article_parts = ArticleParts.objects.filter(article=item.article)
                for article_part in article_parts:
                    # Obtengo la pieza y su cantidad
                    part = article_part.part
                    quantity_part = article_part.quantity
                    # Multiplico la cantidad de articulos vendidos por la cantidad de piezas que conforman al articulo
                    part.reduce_stock(item.quantity * quantity_part)

            order.status = delivered_status
            order.save()
            return JsonResponse({'status': 'success', 'message': 'ok'})

    except Exception as e:

        return JsonResponse({'status': 'error', 'message': 'error'})


def nextDeliveries(request):
    orders_list = []
    today = date.today()
    orders = Order.objects.filter(delivery_date__gte=today)
    for order in orders:
        if order.status.id != 2:
            orders_list.append(order.toJSON())

    return JsonResponse(orders_list, safe=False)


def getShortfalls(request):
    out_of_stock = []
    # Obtengo las ordenes no entregadas
    orders_undelivered = Order.get_undelivered_orders().prefetch_related('articles__article')

    for order in orders_undelivered:
        order_items = order.get_order_items()
        for item in order_items:
            if item.quantity >= item.article.stock:
                out_of_stock.append(item.toJSON())

    return JsonResponse(out_of_stock, safe=False)

