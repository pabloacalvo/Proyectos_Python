from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article

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
<<<<<<< Updated upstream
    return render(request, 'index.html',{
        'title':'Pagina de inicio',
        'mi_variable': 'soy un dato que esta en la vista',
        'nombre':nombre,
        'lenguajes':lenguajes,
        'years':hasta
    })
=======
    return render(request, 'index.html')


def crear_articulo(request, title,content,public):
    articulo = Article(
        title=title,
        content=content,
        public = public
    )

    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")


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


def articulos(request):

    #todos
    articulos = Article.objects.all()
    #ordenados por
    #articulos = Article.objects.order_by('id')
    #limit
    #articulos = Article.objects.order_by('id')[3:4]

    """ __lookup type es una opcion mas para aplicar al filtro en este caso __contains equivale al LIKE en sql,
        __exact valor exacto
        __iexact valor exacto pero no es key sensitive
    """
    articulos = Article.objects.filter(id__gt=8)

    return render(request, 'articulos.html',{
        'articulos':articulos
    })


def borrar_articulo(request,id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')
>>>>>>> Stashed changes
