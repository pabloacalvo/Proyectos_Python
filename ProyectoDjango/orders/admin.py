from django.contrib import admin
from .models import Order,OrderItem, OrderStatus

class OrderStatusAdmin(admin.ModelAdmin):
    model = OrderStatus
    list_display = ('id','name_status')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['article']
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields = ('client', 'created_at')
    list_filter = ('status', 'client')
    list_display = ('status','id',
                    'client',
                    'created_at',
                    'updated_at')
    ordering = ('-created_at',)
    inlines = [OrderItemInline]



admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)