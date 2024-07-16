from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.index, name='index'),
    path('articulos/', views.articles, name='list_articles'),
    path('categoria/<int:category_id>', views.category, name='category'),
    path('articulo/<int:article_id>', views.get_article, name='article'),
    path('partes/', views.articlesParts, name='list_parts'),
    path('create-article/', views.createArticle, name='create_article'),
    path('editar-articulo/<int:article_id>', views.editArticle, name='edit_article'),
]