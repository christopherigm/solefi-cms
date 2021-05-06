from django.contrib import admin
from info_grid.models import (
    InfoGrid,
    InfoGridItem
)

# Register your models here.

class InfoGridItemAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'order',
        'icon',
        'info_grid'
    ]
admin.site.register(InfoGridItem, InfoGridItemAdmin)

class InfoGridAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'page'
    ]
admin.site.register(InfoGrid, InfoGridAdmin)
