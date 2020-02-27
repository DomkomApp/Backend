from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('id', 'user', 'comment_field')


class CommentCreateSerializer(serializers.Serializer):
    comment_field = serializers.CharField()


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'text', 'date')
