from django.shortcuts import render, get_object_or_404, redirect
from .models import OrderItem, OrderStatus, Order
from .forms import OrderCreateForm, OrderItemsForm, OrderItemsFormSet
from cart.cart import Cart
from decimal import Decimal
# Create your views here.

def create_order(request):
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
                OrderItem.objects.create(
                    order=order,
                    article=article['article'],
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
                      'cart': cart,
                      'form': form  # Pasa el formulario al contexto
                  })


def get_orders(request):
    orders = Order.objects.all()

    return render(request, 'orders/orders_view.html', {
        'orders': orders
    })

def get_orderItems(request, order_id):
    # Obtener el pedido
    order = get_object_or_404(Order, id=order_id)
    # Obtener todos los artículos del pedido
    order_items = OrderItem.objects.filter(order=order)

    return render(request, 'orders/order_modalDetails.html', {
        'order': order,
        'order_items': order_items
    })

def delete_order(request,order_id):
    order = get_object_or_404(Order, id=order_id)

    order.delete()

    return redirect('orders:get_orders')


from decimal import Decimal


def edit_order(request, order_id):
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
            print(order_form.errors)
            print(formset.errors)
    else:
        order_form = OrderCreateForm(instance=order)
        formset = OrderItemsFormSet(instance=order)

    return render(request, 'orders/order_modalDetails.html', {
        'form': order_form,
        'formset': formset,
        'order_id': order_id
    })



