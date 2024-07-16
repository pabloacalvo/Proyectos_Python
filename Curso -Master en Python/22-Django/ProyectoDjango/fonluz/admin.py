from django.contrib import admin
from .models import Category, Article, Parts, ArticleParts
from decimal import Decimal

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


class ArticlePartsInline(admin.StackedInline):
    model = ArticleParts
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    # Agrupacion de secciones en el form
    fieldsets = [
            ('Datos del producto', {'fields': ['article_code', 'article_name','category','stock','image','article_type','public']}),
            ('Valores del producto', {'fields': ['cost','margin', 'price']})
        ]
    # Campos que no se van a mostrar
    readonly_fields = ('description', 'updated_at', 'created_at', 'modify_user')
    # Filtro de busqueda
    search_fields = ('article_code', 'article_name', 'description')
    list_filter = ('article_type', 'category', 'stock')
    # Formato del listado de articulos
    list_display = ('article_code', 'article_name',
                    'cost', 'price',
                    'stock', 'updated_at')

    ordering = ('-updated_at',)

    # Permite editar el modelo relacionado dentro del mismo formulario
    inlines = [ArticlePartsInline]

    def save_model(self, request, obj, form, change):
        margin_value = form.cleaned_data.get('margin')
        cost = form.cleaned_data.get('cost')
        if not obj.modify_user_id:
            obj.modify_user_id = request.user.id
        self.calculated_price(obj)


    def calculated_price(self, obj):
        if obj.pk:
            print('CALCULANDO COSTO')
            total_cost = sum(article_part.part.cost * article_part.quantity for article_part in obj.articleparts_set.all())
            print(total_cost)
            obj.cost = total_cost
            # Paso del decimal ej: 20,00 a 0,20
            desired_margin = obj.margin / Decimal(100)
            # Costo / 1-0,20 por ejemplo costo/0,80
            obj.price = total_cost / (1 - desired_margin)
            obj.save()

class ArticlePartsAdmin(admin.ModelAdmin):
    list_display = ('part', 'article', 'quantity', 'part_stock')

    def part_stock(self, obj):
        return obj.part.stock

    part_stock.short_description = 'Stock de la pieza'

    def save_model(self, request, obj, form, change):
        if not obj.modify_user_id:
            obj.modify_user_id = request.user.id
        obj.save()
        ArticleAdmin.calculated_price(obj)



# Register your models here.
admin.site.register(Parts)
admin.site.register(ArticleParts, ArticlePartsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
