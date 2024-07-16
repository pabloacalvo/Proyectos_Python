from decimal import Decimal
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, ArticleParts, Parts
from django.core.paginator import Paginator
from .forms import ArticleForm, ArticlePartsFormSet

# Create your views here.

def index(request):
    return render(request, 'fonluz/index.html',
                  {'title': 'Inicio'})

def articles(request):
    # Obtener articulos
    articles = Article.objects.all()
    # Paginar los articulos aca se pone el parametro de cuantos articulos por pagina
    paginator = Paginator(articles, 10)
    # Obtener numero de pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request,'articles/articles_list.html', {
        'title':' Articulos',
        'articles': page_articles
    })

def category(request, category_id):
    # Devuelve pagina 404 si el ID en la url no existe
    category = get_object_or_404(Category, id=category_id)

    # Filtrar articulos de esa categoria,
    articles = Article.objects.filter(category=category_id)

    return render(request, 'categories/category.html', {
        'category': category
    })

def get_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    parts = ArticleParts.objects.filter(article=article_id)

    return render(request, 'articles/article_modalDetails.html', {
        'article':article
    })


def articlesParts(request):
    filters = {'Nombre': 'name',
               'Codigo': 'id',
               'Stock(menor/igual que)': 'stock'
               }
    # Obtener articulos
    articles_parts = Parts.objects.all()

    filterType = request.GET.get('filterType')
    filterTxt = request.GET.get('filterValue')

    if filterTxt:
        if filterType == 'Nombre':
            articles_parts = Parts.objects.filter(name__contains=filterTxt)
        elif filterType == 'Codigo':
            articles_parts = Parts.objects.filter(id=int(filterTxt))
        elif filterType == 'Stock(menor/igual que)':
            articles_parts = Parts.objects.filter(stock__lte=int(filterTxt))

        paginator = Paginator(articles_parts, 10)
        page = request.GET.get('page')
        page_articles_parts = paginator.get_page(page)

        return render(request, 'articles/article_parts.html', {
            'title': 'Partes',
            'filters': filters,
            'parts': page_articles_parts,
            'filterTxt': filterTxt,
            'filterType': filterType
        })
    else:
        paginator = Paginator(articles_parts, 10)
        page = request.GET.get('page')
        page_articles_parts = paginator.get_page(page)

        return render(request, 'articles/article_parts.html', {
            'title': 'Partes',
            'filters': filters,
            'parts': page_articles_parts
        })

def createArticle(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        formset = ArticlePartsFormSet(request.POST)
        if article_form.is_valid() and formset.is_valid():
            # Obtenemos el objecto de Article
            article = article_form.save(commit=False)
            # Obtemenos una lista de objetos ArticleParts
            article_parts = formset.save(commit=False)
            # Obtenemos el costo total sumando el costo de cada parte
            total_cost = sum(article_part.part.cost * article_part.quantity for article_part in article_parts)
            # Asignamos el costo obtenido al articulo
            article.cost = total_cost
            # Parseamos el margen
            desired_margin = article.margin / Decimal(100)
            # Costo / 1-0,20 por ejemplo costo/0,80
            article.price = total_cost / (1 - desired_margin)
            # Guardamos el articulo luego de obtener su precio basándonos en el costo de sus partes y margen
            article.save()
            for part in article_parts:
                part.article = article
                part.save()
                # Crear mensaje flash (sesion que solo se muestra 1 vez)
                messages.success(request, f'El articulo se creo correctamente {article.article_name}')

            return redirect('list_articles')
    else:
        article_form = ArticleForm()
        formset = ArticlePartsFormSet()

    return render(request, 'articles/create_article.html', {'form': article_form,'formset':formset})


def editArticle(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        print(request.POST)
        article_form = ArticleForm(request.POST, instance=article)
        formset = ArticlePartsFormSet(request.POST, instance=article)

        if article_form.is_valid() and formset.is_valid():

            article = article_form.save(commit=False)
            article_parts = formset.save(commit=False)
            print(article_parts)  # Verifica que esto muestra las instancias de ArticleParts

            total_cost = sum(article_part.part.cost * article_part.quantity for article_part in article_parts if
                             article_part.pk is not None)
            article.cost = total_cost
            desired_margin = article.margin / Decimal(100)
            article.price = total_cost / (1 - desired_margin)

            article.save()
            for part in article_parts:
                if part.pk is not None:
                    part.article = article
                    part.save()
                elif formset.deleted_forms:
                    for deleted_form in formset.deleted_forms:
                        if deleted_form.instance.pk:
                            deleted_form.instance.delete()
            messages.success(request, f'El artículo se actualizó correctamente {article.article_name}')
            return redirect('list_articles')
        else:
            print("Article form errors:", article_form.errors)
            print("Formset errors:", formset.errors)
            for form in formset:
                print("Form errors:", form.errors)
    else:
        article_form = ArticleForm(instance=article)
        formset = ArticlePartsFormSet(instance=article)

    return render(request, 'articles/edit_article.html', {'form': article_form, 'formset': formset})




