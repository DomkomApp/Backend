from django.contrib import admin

from .models import CustomUser

class CustomerUserAdmin(admin.ModelAdmin):
    class Meta:
        model = CustomUser
        exclude = ''
