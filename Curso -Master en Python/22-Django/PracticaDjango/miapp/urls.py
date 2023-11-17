from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('inicio/', views.index, name='index'),
        path('hola-mundo/', views.index, name='hola_mundo'),
        path('pagina-pruebas/', views.pagina, name='pagina'),
        path('pagina-pruebas/<int:redirigir>', views.pagina, name='pagina'),
        path('contacto-dos/', views.contacto, name='contacto'),
        path('contacto/<str:nombre>/',views.contacto, name='contacto'),
        path('contacto/<str:nombre>/<str:apellidos>', views.contacto, name='contacto')

]