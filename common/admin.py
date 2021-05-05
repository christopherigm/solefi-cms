from django.contrib import admin
from common.models import (
    Country,
    State,
    City
)

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'code',
        'enabled',
    ]
    search_fields = ('name','code')
    list_filter = ('enabled',)
admin.site.register(Country, CountryAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'code',
        'country',
        'enabled'
    ]
    search_fields = ('name','country')
    list_filter = ('enabled','country')
admin.site.register(State, StateAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'state',
        'enabled'
    ]
    search_fields = ('name','state')
    list_filter = ('enabled','state','state__country')
admin.site.register(City, CityAdmin)
