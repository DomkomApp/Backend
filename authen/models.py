from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




class CustomUser(AbstractUser):
    validation_code = models.CharField(max_length=5,null=True,blank=True)
    @classmethod
    def create(cls,username,password,validation_code):
        custom_user = cls.objects.create(username=username,password=password,validation_code=validation_code)
        return custom_user

    class Meta:
        verbose_name = 'Регистрация номера'
        verbose_name_plural = 'Регистрация номеров'
