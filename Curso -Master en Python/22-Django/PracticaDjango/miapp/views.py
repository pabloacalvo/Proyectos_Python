from django.shortcuts import render, HttpResponse, redirect
from .models import Article
from django.db.models import Q
from .forms import FormArticle, RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# MVC= MODELO VISTA CONTROLADOR se ejecutan acciones (métodos) es lo mismo que MVT solo que a la vista se la llama template y al controlador vista.
# MVT= MODELO VISTA TEMPLATE se ejecutan acciones (métodos) en Django las vista "views"  son el controlador


def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('contacto', nombre='Pablo', apellidos='Calvo')
    return render(request, 'pagina.html', {
        'texto': 'Este es mi texto',
        'lista': [1, 2, 3]
    })


def contacto(request, nombre='', apellidos=''):
    html=''
    if nombre and apellidos:
        html += '<p>El nombre completo es:</p>'
        html += f'<h3>{nombre} {apellidos}</h3>'
    return HttpResponse(layout+f'<h2>Contacto</h2>'+html)



layout = """
<h1>Sitio web con Django</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/web">Web</a>
    </li>
     <li>
        <a href="/contacto">Contacto</a>
    </li>

</ul>
<hr/>

"""


def index(request):
    """
    html =
        <h1>Inicio</h1>
        <p> Años hasta el 2050:</p>
        <ul>

        year = 2021
        while year <= 2050:
            html += "<h3>Este es el: </h3>" + "<li>" + str(year) + "</li>"
            year += 1

        html += "</ul>"
    """

    year = 2021
    hasta = range(year,2050)
    nombre = 'Pablo Calvo'
    lenguajes = ['JavaScript','Python','PHP','Java']

    # return HttpResponse(layout+html) #se concateca layout para que aparezca en todas las páginas

    return render(request, 'index.html', {
        'title':'Pagina de inicio',
        'mi_variable': 'soy un dato que esta en la vista',
        'nombre':nombre,
        'lenguajes':lenguajes,
        'years':hasta
    })

    #return render(request, 'index.html')

@login_required(login_url='login')
def crear_articulo(request, title,content,public):
    articulo = Article(
        title=title,
        content=content,
        public=public
    )

    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")

def save_article(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        if len(title) <= 5:
            return HttpResponse('El titulo es muy pequeño')

        articulo = Article(
            title=title,
            content=content,
            public=public
        )
        articulo.save()
        return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")
    else:
        return HttpResponse('<h2>No se ha podido crear el articulo</h2>')




def create_article(request):
    return render(request, 'create_article.html')

@login_required(login_url='login')
def create_full_article(request):

    if request.method == 'POST':
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data
            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title=title,
                content=content,
                public=public
            )
            articulo.save()
            # Crear mensaje flash (sesion que solo se muestra 1 vez)
            messages.success(request, f'El articulo se creo correctamente {articulo.id}')

            return redirect('articulos')
    else:
        formulario = FormArticle()

    return render(request, 'create_full_article.html', {'form': formulario})

def articulo(request):
    try:
        articulo = Article.objects.get(pk=6)
        response = f"Articulo: <br/>{articulo.id}. {articulo.title}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)

def editar_articulo(request, id):

    articulo = Article.objects.get(pk=id)

    articulo.title = 'Batman'
    articulo.content = 'Pelicula del 2017'
    articulo.public = True
    articulo.save()

    return HttpResponse(f"El articulo {articulo.title} fue editado")

@login_required(login_url='login')
def articulos(request):

    # UTILIZAR ESTA CAPA DE ABSTRACCION DE DJANGO TIENE COMO BENEIFICIO QUE AL CAMBIAR DE MOTOR DE BASE DE DATOS
    # NO VA SER NECESARIO UN CAMBIO EN EL CODIO
    #todos
    articulos = Article.objects.all().order_by('-id')

    #ordenados por
    #articulos = Article.objects.order_by('id')
    #limit
    #articulos = Article.objects.order_by('id')[3:4]
    #articulos = Article.objects.filter(Q(title__contains='escencial') | Q(title__contains='1'))

    """ __lookup type es una opcion mas para aplicar al filtro ejemplos:
        __contains equivale al LIKE en sql,
        __exact valor exacto
        __iexact valor exacto pero no es key sensitive
        __gt mas grande que
        __gte mayores o iguales
        __lt menores que
        __lte menores o iguales que
    """
    #articulos = Article.objects.filter(title='Primer articulo')
    #articulos = Article.objects.filter(id__gt=8)

    #articulos = Article.objects.filter(title__contains="Articulo").exclude(public=False)

    # FILTROS UTILIZANDO SQL DIRECTAMENTE
    #articulos_sql = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Producto escencial'")

    return render(request, 'articulos.html',{
        'articulos':articulos
    })

@login_required(login_url='login')
def borrar_articulo(request,id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        register_form = RegisterForm()
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                return redirect('/inicio')

        return render(request, 'register.html', {
            'title':'Registro',
            'register_form':register_form
        })

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.warning(request,'No te has identificado correctamente')

        return render(request, 'login.html', {'title':'Identificate'})

def logout_user(request):
    logout(request)

    return redirect('login')