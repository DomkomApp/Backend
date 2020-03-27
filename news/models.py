from django.db import models
from authen.models import CustomUser


class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=128)
    image = models.ImageField(verbose_name='Картинка', upload_to="media/", null=True, blank=True)
    text = models.TextField(verbose_name='Текст', max_length=1000)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='comment')
    comment_field = models.CharField(verbose_name='Коментарий', max_length=250)
    news = models.ForeignKey(News, verbose_name='Новости', on_delete=models.PROTECT, related_name='comment')

    def __str__(self):
        return f'{self.user}-{self.news}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
