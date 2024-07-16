from django.contrib import admin
from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
# Register your models here.

# Configurar el titilo del panel
title = 'Practica Django - Calvo Pablo'
admin.site.site_header = title
admin.site_site_title = title
admin.site.index_title = 'Panel de gestion'