from django.urls import path
from . import views

urlpatterns = [
        #path('admin/', admin.site.urls),
        path('', views.index, name='index'),
        path('inicio/', views.index, name='index'),
        path('hola-mundo/', views.index, name='hola_mundo'),
        path('pagina-pruebas/', views.pagina, name='pagina'),
        path('pagina-pruebas/<int:redirigir>', views.pagina, name='pagina'),
        path('contacto-dos/', views.contacto, name='contacto'),
        path('contacto/<str:nombre>/',views.contacto, name='contacto'),
        path('contacto/<str:nombre>/<str:apellidos>', views.contacto, name='contacto'),
        path('crear-articulo/<str:title>/<str:content>/<str:public>',views.crear_articulo, name='crear_articulo'),
        path('articulo/',views.articulo, name='articulo'),
        path('editar-articulo/<int:id>', views.editar_articulo, name='editar_articulo'),
        path('articulos/',views.articulos,name='articulos'),
        path('borrar-articulo/<int:id>', views.borrar_articulo,name='borrar')

]