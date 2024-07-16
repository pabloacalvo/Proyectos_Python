
from django.urls import path
from . import views

# Esto debe estar para registrar el namespace
app_name = 'orders'

urlpatterns = [
    path('create/', views.create_order, name='order_create'),
    path('view-orders/', views.get_orders, name='get_orders'),
    path('order_items/<int:order_id>', views.get_orderItems, name='order_items'),
    path('order-delete/<int:order_id>', views.delete_order, name='delete_order'),
    path('order-edit/<int:order_id>', views.edit_order, name='edit_order'),
]