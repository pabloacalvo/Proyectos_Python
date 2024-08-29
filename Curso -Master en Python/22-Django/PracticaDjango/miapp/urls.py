from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
        #path('admin/', admin.site.urls),
        path('', views.index, name='index'),
        path('inicio/', views.index, name='index'),
        path('hola-mundo/', views.index, name='hola_mundo'),
        path('pagina-pruebas/', views.pagina, name='pagina'),
        path('pagina-pruebas/<int:redirigir>', views.pagina, name='pagina'),
        path('contacto-dos/', views.contacto, name='contacto'),
        path('contacto/<str:nombre>/', views.contacto, name='contacto'),
        path('contacto/<str:nombre>/<str:apellidos>', views.contacto, name='contacto'),
        path('crear-articulo/<str:title>/<str:content>/<str:public>',views.crear_articulo, name='crear_articulo'),
        path('articulo/', views.articulo, name='articulo'),
        path('editar-articulo/<int:id>', views.editar_articulo, name='editar_articulo'),
        path('articulos/', views.articulos, name='articulos'),
        path('borrar-articulo/<int:id>', views.borrar_articulo, name='borrar'),
        path('save-article/', views.save_article, name='save'),
        path('create-article/', views.create_article, name='create'),
        path('create-full-article/', views.create_full_article, name='create_full'),
        path('registro/', views.register_page, name='register'),
        path('login/', views.login_page, name='login'),
        path('logout/',views.logout_user,name='logout'),

]


# Configuracion para cargar imagenes
if settings.DEBUG:
        from django.conf.urls.static import static
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)