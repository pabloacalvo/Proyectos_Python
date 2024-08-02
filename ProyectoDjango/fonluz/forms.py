# forms.py
from django import forms
from django.forms import formset_factory, inlineformset_factory
from django_select2.forms import Select2MultipleWidget, Select2Widget
from .models import Article, Parts, ArticleParts

"""
Se crean dos clases de form : 
ArticleParts para crear la pieza y cantidad.
ArticleForm para crear el articulo
Luego se crea una intancia de inlineformset_factory con el modelo principal, modelo secundario(tabla intermedia y el formulario a mostrar)
"""


class ArticlePartsForm(forms.ModelForm):
    class Meta:
        model = ArticleParts
        fields = ['part', 'quantity']
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Cantidad necesaria'}),
            'part': Select2Widget(attrs={'class': 'form-control mb-3', 'placeholder': 'Pieza'})
        }


class ArticleForm(forms.ModelForm):
    quantity = forms.IntegerField(label='Cantidad', required=False, min_value=0)
    quantity.widget.attrs.update({'placeholder': 'Cantidad'})

    class Meta:
        model = Article
        fields = ['article_code', 'article_name', 'category', 'image', 'stock', 'cost', 'tax_iva',
                  'margin', 'price', 'public', 'article_type', 'necessary_parts']
        widgets = {'article_code': forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Codigo del articulo'}),
            'article_name': forms.TextInput(
                attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre del articulo'}),
            'article_type': Select2Widget(
                attrs={'id': 'selectType', 'class': 'form-control mb-3', 'placeholder': 'Tipo de articulo'}),
            'category': Select2Widget(
                attrs={'id': 'selectCategory', 'class': 'form-control mb-3', 'placeholder': 'Categoria'}),
            'cost': forms.TextInput(
                attrs={'class': 'form-control mb-3', 'placeholder': 'Costo'}),
            'price': forms.TextInput(
                attrs={'class': 'form-control mb-3', 'placeholder': 'Precio'}),
            'stock': forms.TextInput(
                attrs={'class': 'form-control mb-3', 'placeholder': 'Stock'}),
            'margin': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Margen de ganancia'}),
            'necessary_parts': Select2Widget(
                attrs={'id': 'selectParts', 'class': 'form-control mb-3', 'placeholder': 'Partes necesarias'})
        }

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        # Marcar el campo necessary_parts como no requerido
        self.fields['necessary_parts'].required = False
        self.fields['cost'].required = False
        self.fields['price'].required = False


class PartForm(forms.ModelForm):

    class Meta:
        model = Parts
        fields = ['name', 'stock', 'cost']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre de la pieza'}),
            'stock': forms.TextInput(
                attrs={'class': 'form-control mb-3', 'placeholder': 'Stock'}),
            'cost': forms.TextInput(
                attrs={'class': 'form-control mb-3', 'placeholder': 'Costo'})
        }


ArticlePartsFormSet = inlineformset_factory(Article, ArticleParts, form=ArticlePartsForm)
