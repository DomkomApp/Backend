from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('user', views.MyUserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
