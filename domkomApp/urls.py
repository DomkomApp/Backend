"""domkomApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.views.static import serve

# Imports for unregister
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group

from rest_framework.authtoken import views

admin.site.site_header = 'Domkom Administration'


# Unregistered models
# admin.site.unregister(Group)
# admin.site.unregister(Token)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', include('users.urls')),
    path('house-register/', include('housereg.urls')),
    path('news/', include('news.urls')),
    url('auth/', include('authen.urls')),
    url('service/', include('service.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
