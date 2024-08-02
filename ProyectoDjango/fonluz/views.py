import json
from decimal import Decimal
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, ArticleParts, Parts
from django.core.paginator import Paginator
from .forms import ArticleForm, ArticlePartsFormSet, PartForm



def index(request):
    # Pagina de inicio muestra tabla con productos pedidos con faltantes y proximas entregas
    # urls en la app orders
    return render(request, 'layout/index.html', {'title':'Inicio'})

def articles(request):

    return render(request,'articles/articles_list2.html', {
        'title':'Gestion de productos'
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
    article = get_object_or_404(Article.objects.prefetch_related('articleparts_set__part'), id=article_id)

    return render(request, 'articles/article_modalDetails.html', {
        'article': article
    })

def getChangesArticles(request):
    data = []
    articles = Article.get_latest_price_changes()
    for article in articles:
        data.append(article.toJSON())

    return JsonResponse(data, safe=False)

def parts(request):

    return render(request, 'parts/parts_list.html',{'title':'Detalle de piezas'})

"""def articlesParts(request):
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
        })"""

def getParts(request):
    data = []
    parts = Parts.objects.all()
    for part in parts:
        data.append(part.toJSON())

    return JsonResponse(data,safe=False)

def getPartsSlowStock(request):
    data = []
    parts = Parts.get_low_stock()
    for part in parts:
        data.append(part.toJSON())
    return JsonResponse(data,safe=False)

def editPart(request, part_id):
    part = get_object_or_404(Parts, id=part_id)
    if request.method == 'POST':
        form = PartForm(request.POST, instance=part)
        if form.is_valid():
            # Verifico que haya cambios en el formulario
            if form.has_changed():
                form.save()
                # Verifico si hay cambios en el costo
                if 'cost' in form.changed_data:
                    # Obtener los articulos que contienen esa pieza que cambio su costo
                    affected_articles = Article.objects.filter(articleparts__part=part).distinct()
                    # Recorrodo esa lista de articulos
                    for article in affected_articles:
                        # Recalculo su costo
                        new_cost = article.calculate_cost()
                        # Recalculo su precio de venta
                        new_price = article.calculate_price()
                        # Hago el update de su costo y precio
                        article.cost = new_cost
                        article.price = new_price
                        # Hago el commit
                        article.save()
                    # Crear mensaje para los articulos modificados
                    if affected_articles.exists():
                        affected_articles_names = ', '.join(article.article_name for article in affected_articles)
                        messages.success(request,f"Los siguientes artículos han sido modificados en su precio: {affected_articles_names}")
                # Si no hubo cambios en el costo de la pieza
                else:
                    messages.info(request, "Pieza actualizada, sin cambios en su valor.")
                    print("Messages:", list(messages.get_messages(request)))  # Debugging line

            return redirect('list_parts')

        # Formulario no es valido
        else:
            form = PartForm(instance=part)

    else:
        form = PartForm(instance=part)
    return render(request, 'parts/part_modalDetails.html', {'formpart': form, 'part_id': part_id})

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

    return render(request, 'articles/create_article.html',
                  { 'form': article_form,
                            'formset':formset,
                            'title':'Crear nuevo producto'})


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

            total_cost = Decimal(0)
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    part = form.cleaned_data['part']
                    quantity = form.cleaned_data['quantity']
                    total_cost += part.cost * quantity

            article.cost = total_cost
            desired_margin = article.margin / Decimal(100)
            article.price = total_cost * (1 + desired_margin)

            article.save()

            for part in formset.save(commit=False):
                part.article = article
                part.save()

            for part in formset.deleted_forms:
                if part.instance.pk:
                    part.instance.delete()

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


def productList(request):
    data = []
    articles = Article.objects.all()
    for article in articles:
        data.append(article.toJSON())

    # Parametro safe=false porque JsonResponse espera un objeto dict y le estoy pasando una lista de dict
    return JsonResponse(data,safe=False)





