from django import forms
from django.forms import inlineformset_factory, DateInput
from django_select2.forms import Select2Widget

from .models import Order, OrderStatus, OrderItem


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class OrderItemsForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['id','article','price', 'quantity']
        widgets = {
            'id': forms.HiddenInput(),
            'article': forms.HiddenInput(),
            'quantity': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Cantidad necesaria'}),
            'price': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Precio del artículo'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Puedes personalizar más si es necesario



class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['client','status','discount','delivery_date']
        widgets = {
            'client': Select2Widget(attrs={
                    'class': 'form-control custom-width',
                    'required':'required',
                    'placeholder':'Cliente'
                }),
                    'status': Select2Widget(attrs={
                    'class': 'form-control custom-width',
                    'data-minimum-input-length': '0',
                    'data-theme': 'default',
                    'data-allow-clear': 'true',
                    'data-placeholder': '',
                    'required': 'required',
                }),
            'discount': forms.TextInput(
             attrs={'class': 'form-control custom-width',
                    'placeholder': 'Descuento'}),
            'delivery_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date', 'class': 'form-control picker-fecha-entrega', 'placeholder': 'Fecha de entrega'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Setear el status predeterminado al momento de confirmar el pedido
        default_status = OrderStatus.objects.get(pk=1)
        # Se va mostrar este valor en el campo
        self.fields['status'].initial = default_status

OrderItemsFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=0)
