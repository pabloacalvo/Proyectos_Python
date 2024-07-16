from django.db import models
from django.utils import timezone
from clients.models import Client
from fonluz.models import Article
from decimal import Decimal


class OrderStatus(models.Model):
    name_status = models.CharField(verbose_name='Nombre del estado',unique=True,max_length=50)
    description = models.CharField(verbose_name='Descripcion',null=True,blank=True,max_length=150)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return f'{self.name_status}'

class Order(models.Model):
    client = models.ForeignKey(Client, verbose_name='Cliente',on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Ultima actualizacion')
    status = models.ForeignKey(OrderStatus,verbose_name='Estado',on_delete=models.SET_NULL, null=True,blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='Descuento',default=0.00,blank=True,null=True)
    total = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Total a pagar', default=0.00, blank=True, null=True)


    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]


    def __str__(self):
        return f'Pedido {self.id}'


    def get_discountAmount(self):
        discount = self.discount / Decimal(100)
        total_discount = self.total * discount
        return total_discount.__round__(2)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='articles', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='order_articles', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{str(self.id)}'

    def calcular_total(self):
        total = self.price * self.quantity
        return total

