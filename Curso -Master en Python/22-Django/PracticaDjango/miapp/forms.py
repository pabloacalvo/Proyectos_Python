from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormArticle(forms.Form):
    # Se puede personalizar widget al momento de crear el campo
    title = forms.CharField(label='Titulo',
                            max_length=20,
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder':'Ingrese el titulo','class':'titulo_form_article'}),
                            validators=[validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
                                        validators.RegexValidator('^[A-Za-z0-9 ]*$', 'El titulo contiene caracteres no permitidos', 'invalid_title')])
    content = forms.CharField(label='Contenido',
                              widget=forms.Textarea,
                              required=False,
                              validators=[validators.MaxLengthValidator(20, 'La descripcion es muy larga')])

    # Se puede usar el UPDATE
    content.widget.attrs.update({
        'placeholder': 'Ingresa una descripcion', 'class': 'titulo_form_article'
    })

    public_options = [(0,'No'),(1,'Si')]
    public = forms.TypedChoiceField(choices=public_options, label='Estado de publicacion')

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']