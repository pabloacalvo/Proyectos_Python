
from django.urls import path
from . import views

# Esto debe estar para registrar el namespace
app_name = 'orders'

urlpatterns = [
    path('order/order_list/', views.orderList, name='order_list'),
    path('order/create/', views.createOrder, name='order_create'),
    path('order/view-orders/', views.getOrders, name='get_orders'),
    path('order/order_items/<int:order_id>', views.getOrderItems, name='order_items'),
    path('order/order-delete/<int:order_id>', views.deleteOrder, name='delete_order'),
    path('order/order-edit/<int:order_id>', views.editOrder, name='edit_order'),
    path('order/deliver/<int:order_id>', views.deliverOrder, name='deliver_order'),
    path('order/next-deliveries/', views.nextDeliveries, name='next_deliveries'),
    path('order/get-shortfalls/', views.getShortfalls, name='get_shortfalls'),
]