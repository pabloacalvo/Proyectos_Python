from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    search_fields = ('dni', 'name','surname')
    list_filter = ('status',)
    list_display = ('name',
                    'surname', 'dni',
                    'email', 'telephone',
                    'address','status')


admin.site.register(Client,ClientAdmin)
