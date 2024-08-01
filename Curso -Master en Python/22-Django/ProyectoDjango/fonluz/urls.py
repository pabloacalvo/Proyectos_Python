from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articulos/', views.articles, name='list_articles'),
    path('categoria/<int:category_id>', views.category, name='category'),
    path('article/<int:article_id>', views.get_article, name='article'),
    path('article/latest-changes/',views.getChangesArticles, name='-articles-latest-changes'),
    path('create-article/', views.createArticle, name='create_article'),
    path('editar-articulo/<int:article_id>', views.editArticle, name='edit_article'),
    path('articles/', views.productList, name='product_list'),
    path('parts/', views.getParts, name='get_parts'),
    path('parts/list/', views.parts, name='list_parts'),
    path('parts/edit/<int:part_id>', views.editPart, name='edit_part'),
    path('parts/get-slow-stock/', views.getPartsSlowStock, name='get-slow-stock'),
]