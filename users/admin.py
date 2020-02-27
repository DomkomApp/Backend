from django.contrib import admin

from .models import *


class CarInline(admin.TabularInline):
    model = Car
    extra = 0


class CarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.fields]

    class Meta:
        model = Car


class OwnerTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OwnerType._meta.fields]

    class Meta:
        model = OwnerType


class RegNumberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomUser._meta.fields]

    class Meta:
        model = CustomUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'address', 'flat', 'floor',
                    'people', 'owner_type']
    inlines = [CarInline]
    list_filter = ['full_name']
    search_fields = ['full_name', 'phone', 'address', 'flat']

    class Meta:
        model = User


admin.site.register(OwnerType, OwnerTypeAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CustomUser)
admin.site.register(User, MyUserAdmin)
