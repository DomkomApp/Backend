from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.MyUserViewSet)
router.register('cars', views.CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
