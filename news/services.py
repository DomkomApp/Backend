from django.db.models import QuerySet
from rest_framework.exceptions import NotFound

from .models import *


class CommentService:
    @classmethod
    def filter(cls, **filters):
        return Comment.objects.filter(**filters)

    @classmethod
    def create_comment(cls, service: News, comment: str, author: CustomUser):
        Comment.objects.create(service=service, comment=comment, user=author)


class AppService:
    @classmethod
    def filter(cls, **filters) -> QuerySet:
        return News.objects.filter(**filters)

    @classmethod
    def get_comments(cls, service_id: int) -> QuerySet:
        service = cls.filter(id=service_id).first()
        if not service:
            raise NotFound
        return CommentService.filter(service_id=service_id)

    @classmethod
    def comment_idea(cls, idea_id: int, comment: str, author: CustomUser):
        service = AppService.filter(id=idea_id).first()
        if not service:
            raise NotFound
        CommentService.create_comment(service, comment, author)
