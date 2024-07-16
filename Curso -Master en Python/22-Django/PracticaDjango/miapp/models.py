from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100,verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to='articles')
    public = models.BooleanField(verbose_name='Publicado?')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True,verbose_name='Creado el')
    update_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name='Editado el')

    class Meta:
        # para asignar el nombre a la tabla
        #db_table = ""
        # nombre singular del elemento
        verbose_name = 'Articulo'
        # nombre plural del elemento
        verbose_name_plural = 'Articulos'
        # Ordenacion de como se muestran los articulos
        #ordering = ['-id'] # descendente
        ordering = ['-created_at']

    # Modificar el valor que se muestra en la lista de articulos
    def __str__(self):
        if self.public:
            publico = '(Publicado)'
        else:
            publico = '(Privado)'
        return f'{self.title} {publico}'

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'