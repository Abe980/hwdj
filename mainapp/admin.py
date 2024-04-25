from decimal import Decimal
from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description='Apply promotion')
def apply_promotion(modeladmin, request, queryset):
    for order in queryset:
        order.total_price = order.total_price * Decimal(0.9)
        order.save()
    

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'adress']
    ordering = ['name']
    search_fields = ['name', 'email', 'phone', 'adress']
    search_help_text = 'Find Name, email, phone, adress'
    

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count']
    ordering = ['-price', 'count', 'name']
    list_filter = ['count']
    search_fields = ['name', 'descirption']
    search_help_text = 'Find name and description'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price']
    actions = [apply_promotion]
    


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)