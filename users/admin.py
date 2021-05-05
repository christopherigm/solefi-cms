from django.contrib import admin
from users.models import (
  UserAddress,
  UserProfile
)

# Register your models here.

class UserAddressAdmin(admin.ModelAdmin):
    list_display = [
        'alias',
        'city',
        'enabled'
    ]
    search_fields = ('alias',)
    list_filter = ('enabled','city')
admin.site.register(UserAddress, UserAddressAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'language'
    ]
    list_filter = ('language',)
admin.site.register(UserProfile, UserProfileAdmin)
