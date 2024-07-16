from .models import Category, Article

def get_categories(request):
    # Obtener articulos publicados y obtener la lista de los Id de la categoria
    categories_with_articles = Article.objects.all().values_list('category', flat=True)

    # Obtener categorias que su id exista en
    # categories_with_articles para evitar mostrar categorias sin articulos
    categories = Category.objects.filter(id__in=categories_with_articles).values_list('id', 'name')

    return {
        'categories': categories,
        'categories_with_articles': categories_with_articles
    }
