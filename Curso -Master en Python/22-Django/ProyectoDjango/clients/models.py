from django.db import models
from django.forms import model_to_dict


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    surname = models.CharField(max_length=150, verbose_name='Apellido', blank=True, null=True)
    dni = models.CharField(max_length=11, verbose_name='DNI/CUIT/CUIL',unique=True)
    address = models.CharField(max_length=255, verbose_name='Direccion')
    email = models.EmailField(max_length=155, verbose_name='E-Mail')
    telephone = models.CharField(max_length=20, verbose_name='Telefono')
    created_at = models.DateTimeField(verbose_name='Registrado el',auto_now=False, auto_now_add=True)
    status = models.BooleanField(verbose_name='Estado', default=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


    def __str__(self):
        return f'{self.id} {self.name} {self.surname}'

    def toJSON(self):
        client = model_to_dict(self)
        client['status'] = self.status
        return client