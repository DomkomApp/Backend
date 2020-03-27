from django.contrib import admin

from .models import *


class UserInline(admin.TabularInline):
    model = UsersInHouse
    extra = 0


class HouseAdmin(admin.ModelAdmin):
    list_display = ['address', 'house_number', 'people']
    list_filter = ['house_number']
    search_fields = ['house_number']
    inlines = [UserInline]
    readonly_fields = ['people']

    class Meta:
        model = House


class UsersInHouseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UsersInHouse._meta.fields]
    list_filter = ['house']
    search_fields = ['house__address', 'house__house_number', 'person__phone']

    class Meta:
        model = UsersInHouse


admin.site.register(House, HouseAdmin)
admin.site.register(UsersInHouse, UsersInHouseAdmin)
