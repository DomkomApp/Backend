from rest_framework import status, permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwnerOrReadOnly
from .serializers import ServiceSerializer
# Create your views here.
from news.services import *
from .models import *


class ServiceView(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
