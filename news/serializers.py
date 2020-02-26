from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True,source='*')

    class Meta:
        model = Comment
        fields = ('id','user','comment_field')


class CommentCreateSerializer(serializers.Serializer):
    comment_field = serializers.CharField()
