from django.contrib import admin

from .models import *


class UserInline(admin.TabularInline):
    model = UsersInHouse
    extra = 0


class HouseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in House._meta.fields]
    list_filter = ['house_number']
    search_fields = ['house_number']
    inlines = [UserInline]

    class Meta:
        model = House


class UsersInHouseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UsersInHouse._meta.fields]
    list_filter = ['house']
    search_fields = ['person__full_name', 'house__address', 'house__house_number']

    class Meta:
        model = UsersInHouse


admin.site.register(House, HouseAdmin)
admin.site.register(UsersInHouse, UsersInHouseAdmin)
