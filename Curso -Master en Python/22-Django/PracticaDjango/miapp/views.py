from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# MVC= MODELO VISTA CONTROLADOR se ejecutan acciones (métodos) es lo mismo que MVT solo que a la vista se la llama template y al controlador vista.
# MVT= MODELO VISTA TEMPLATE se ejecutan acciones (métodos) en Django las vista "views"  son el controlador

def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('contacto', nombre='Pablo', apellidos='Calvo')
    return render(request, 'pagina.html')


def contacto(request, nombre='', apellidos=''):
    html=''
    if nombre and apellidos:
        html += '<p>El nombre completo es:</p>'
        html += f'<h3>{nombre} {apellidos}</h3>'
    return HttpResponse(layout+f'<h2>Contacto</h2>'+html)


def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request):
    return render(request, 'pagina.html')

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
    return render(request, 'index.html',{
        'title':'Pagina de inicio',
        'mi_variable': 'soy un dato que esta en la vista',
        'nombre':nombre,
        'lenguajes':lenguajes,
        'years':hasta
    })