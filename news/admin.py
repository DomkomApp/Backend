from django.contrib import admin

from .models import News,Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]

    class Meta:
        model = News


admin.site.register(News, NewsAdmin)
admin.site.register(Comment)
