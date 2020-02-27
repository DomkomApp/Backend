from django.http import Http404
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrReadOnly, IsStaffOrAuthenticatedReadOnly
from .serializers import *
from .models import *


class CarViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request):
        car = self.queryset.all()
        serializer = self.serializer_class(car, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('id is required')

        try:
            car = self.queryset.get(id=pk)
        except Car.DoesNotExist:
            raise Http404
        else:
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class MyUserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = MyUserSerializer

    def get_queryset(self):
        return self.queryset.filter(phone=self.request.user)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get()
        if pk is None:
            raise ParseError('id is required')

        try:
            user = self.queryset.get(id=pk)
        except User.DoesNotExist:
            raise Http404
        else:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
