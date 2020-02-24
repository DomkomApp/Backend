from django.contrib import admin

from .models import *


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
                    'people', 'car', 'car_model', 'car_color', 'owner_type']

    class Meta:
        model = User


admin.site.register(OwnerType, OwnerTypeAdmin)
admin.site.register(CustomUser)
admin.site.register(User, MyUserAdmin)
