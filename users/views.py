from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from .serializers import MyUserSerializer
from .models import User


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MyUserSerializer

    def get(self):
        user = self.queryset.all()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
