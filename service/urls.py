from django.conf.urls import url,include
from service import views
from .views import ServiceView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('service',ServiceView)
urlpatterns = [
    url('',include(router.urls)),
]