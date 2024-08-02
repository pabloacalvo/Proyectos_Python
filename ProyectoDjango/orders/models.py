from django.db import models
from django.forms import model_to_dict
from django.utils import timezone
from clients.models import Client
from django.utils.dateformat import DateFormat
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

    def toJSON(self):
        order_status = model_to_dict(self)
        return order_status

class Order(models.Model):
    client = models.ForeignKey(Client, verbose_name='Cliente',on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Ultima actualizacion')
    delivery_date = models.DateField(verbose_name='Fecha de entrega',null=True,blank=True)
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

    @classmethod # Devuelve los pedidos que no estan entregados
    def get_undelivered_orders(cls):
        delivered_status_id = 2
        return cls.objects.exclude(status_id=delivered_status_id)

    def get_discountAmount(self):
        discount = self.discount / Decimal(100)
        total_discount = self.total * discount
        return total_discount.__round__(2)

    def get_order_items(self):
        return self.articles.all()

    def toJSON(self):
        order = model_to_dict(self)
        if self.client is not None:
            order['client'] = self.client.toJSON()
        else:
            order['client'] = {'name':'Sin definir'}
        order['created_at'] = DateFormat(self.created_at).format('Y-m-d H:i:s')
        order['discount'] = float(self.discount)
        order['total'] = float(self.total)
        order['status'] = self.status.toJSON()
        order['discountAmount'] = float(self.get_discountAmount())
        order['totalAmount'] = float(self.total)
        order['updated_at'] = DateFormat(self.updated_at).format('Y-m-d H:i:s')
        if order['delivery_date'] is not None:
            order['delivery_date'] = DateFormat(self.delivery_date).format('d-m-Y')

        return order

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

    def toJSON(self):
        order_item = model_to_dict(self)
        order_item['price'] = float(self.price)
        order_item['article'] = self.article.toJSON()

        return order_item