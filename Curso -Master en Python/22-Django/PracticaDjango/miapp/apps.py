from django.apps import AppConfig


class MiappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'miapp'
    # Cambia el nombre de la aplicacion en el panel de admin
    verbose_name = 'Aplicacion practica Django'
