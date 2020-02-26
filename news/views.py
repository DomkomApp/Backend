from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import *
from .serializers import *

# Create your views here.

class ServiceCommentsView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        comments = AppService.get_comments(kwargs['pk'])
        data = CommentSerializer(comments, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.data.get('comment')
            idea_id = kwargs['pk']
            AppService.comment_idea(idea_id, comment, request.user)
            return Response('Successfully created', status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
