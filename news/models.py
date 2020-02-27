from django.db import models
from authen.models import CustomUser


class News(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment')
    comment_field = models.CharField(max_length=250)
    news = models.ForeignKey(News, on_delete=models.PROTECT, related_name='comment')

    def __str__(self):
        return f'{self.user}-{self.news}'
