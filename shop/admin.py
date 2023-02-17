from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    list_editable = ['price']


admin.site.register(Item, ItemAdmin)