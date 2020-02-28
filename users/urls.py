from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.MyUserViewSet,basename='create')
router.register('cars', views.CarViewSet)
app_name = 'registration'
urlpatterns = [
    path('', include(router.urls)),
]
