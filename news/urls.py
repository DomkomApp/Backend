from django.conf.urls import url
from django.urls import path, include
from .views import NewsView, NewsCommentsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('news', NewsView)
urlpatterns = [
    path('news/<int:pk>/comments/', NewsCommentsView.as_view(), name='news_comments'),
    path('', include(router.urls)),
]
