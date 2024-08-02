from datetime import date, timedelta
from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.utils.dateformat import DateFormat


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la categoria')
    description = models.CharField(blank=True,null=True,max_length=255, verbose_name='Descripcion')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creada el')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

    def toJSON(self):
        category = model_to_dict(self)
        return category

class Parts(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre de la pieza')
    description = models.CharField(null=True,blank=True,max_length=255, verbose_name='Descripcion')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to='parts')
    stock = models.IntegerField(verbose_name='Stock', default=0)
    cost = models.DecimalField(max_digits=11,decimal_places=2,verbose_name='Costo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creada el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name = 'Pieza'
        verbose_name_plural = 'Piezas'

    def __str__(self):
        return self.name

    def toJSON(self):
        part = model_to_dict(self,exclude=['image'])
        part['updated_at'] = DateFormat(self.updated_at).format('Y-m-d H:i:s')
        part['created_at'] = DateFormat(self.created_at).format('Y-m-d H:i:s')
        part['cost'] = float(self.cost)

        return part

    def stock_value(self):
        value = (self.cost * self.stock).__round__(2)
        return value


    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()
        else:
            raise ValueError("Not enough stock available")

    @classmethod
    def get_low_stock(self):
        parts = Parts.objects.filter(stock__lte=0)
        return parts


class Article(models.Model):
    article_code = models.CharField(unique=True, max_length=100, verbose_name='Codigo')
    article_name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripcion',blank=True,null=True)
    category = models.ForeignKey(Category, verbose_name='Categoria',blank=True, on_delete=models.SET_NULL, null=True, related_name='articles')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to='articles')
    stock = models.IntegerField(verbose_name='Stock')
    cost = models.DecimalField(max_digits=11,decimal_places=2,verbose_name='Costo',null=True,blank=True)
    tax_iva = models.DecimalField(max_digits=4,decimal_places=2,verbose_name='Tipo de iva',choices=[(10.5, "10,5"),(21, "21")],blank=True,null=True)
    margin = models.DecimalField(max_digits=6,decimal_places=2, verbose_name='Margen de ganancia',default=20.00)
    price = models.DecimalField(max_digits=11, decimal_places=2,verbose_name='Precio de venta',null=True,blank=True)
    public = models.BooleanField(verbose_name='Publicado en MercadoLibre',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creada el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    modify_user = models.ForeignKey(User, verbose_name='Creado por', on_delete=models.SET_NULL, null=True, editable=False)
    necessary_parts = models.ManyToManyField(Parts, through='ArticleParts', verbose_name='Partes necesarias')
    article_type = models.BooleanField(verbose_name='Tipo de producto', choices=[(False, "Fabricacion propia"),(True, "Adquirido terminado")],default=False)


    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        # Ordenar como se muestran los articulos en la consulta
        ordering = ['-created_at']

    def __str__(self):
        return self.article_name

    def toJSON(self):
        article = model_to_dict(self, exclude=['image','necessary_parts'])
        article['category'] = self.category.toJSON()
        article['price'] = float(self.price)
        article['margin'] = float(self.margin)
        article['cost'] = float(self.cost)
        article['updated_at'] = DateFormat(self.updated_at).format('d-m-Y H:i:s')

        return article
    def calculate_margin(self):
        margin = ((self.cost * 100) / self.price)
        if self.cost > self.price:
            margin = margin * -1
        return margin

    def calculate_cost(self):
        total_cost = Decimal(0)
        for article_part in self.articleparts_set.all():
            part_cost = article_part.part.cost
            quantity = article_part.quantity
            total_cost += part_cost * quantity

        return total_cost

    def calculate_price(self):
        new_cost = self.calculate_cost()
        margin = self.margin / Decimal(100)
        new_price = new_cost * (1 + margin)

        return new_price

    def stock_value(self):
        value = (self.cost * self.stock)
        return value

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()
        else:
            raise ValueError("Not enough stock available")

    @classmethod
    def get_latest_price_changes(cls, days=2):
        #Obtiene los articulos que cambiaron el precio en los ultimos 7 dias
        recent_date = date.today() - timedelta(days=days)
        articles = cls.objects.filter(updated_at__gte=recent_date).order_by('updated_at')
        return articles


class ArticleParts(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Articulo')
    part = models.ForeignKey(Parts, on_delete=models.CASCADE, verbose_name='Pieza')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Cantidad necesaria')

    class Meta:
        verbose_name = 'Pieza del articulo'
        verbose_name_plural = 'Piezas de los articulos'
        ordering = ['-quantity']

    def __str__(self):
        return f'{self.part} {self.article}'

    def toJSON(self):
        part = model_to_dict(self)
        return part