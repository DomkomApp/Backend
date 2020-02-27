from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import ListCreateAPIView

from .services import *
from .serializers import *

# Create your views here.


class NewsCommentsView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        comments = NewsService.get_comments(kwargs['pk'])
        data = CommentSerializer(comments, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            comment_field = serializer.data.get('comment_field')
            idea_id = kwargs['pk']
            NewsService.comment_idea(idea_id, comment_field, request.user)
            return Response('Successfully created', status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class NewsView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer
