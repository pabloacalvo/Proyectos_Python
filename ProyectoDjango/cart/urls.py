from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('created_cart/', views.created_cart, name='created_cart'),
    #path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('cart/add/', views.cart_add, name='cart_add'),
    path('cart/details/', views.cart_detail_json, name='cart_detail_json'),
    #path('add/<int:article_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:article_id>/', views.cart_remove, name='cart_remove'),
    path('cart/clean/', views.clear_cart, name='cart_clean')
]