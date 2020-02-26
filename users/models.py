from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from authen.models import CustomUser

class OwnerType(models.Model):
    user_type = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Тип владельца'
        verbose_name_plural = 'Типы владельцев'

    def __str__(self):
        return self.user_type


class User(models.Model):
    phone = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='user_profile')
    full_name = models.CharField(max_length=128, null=False, blank=False)
    address = models.CharField(max_length=128)
    owner_type = models.ForeignKey(OwnerType, on_delete=models.CASCADE, default=None, null=True, related_name='owner_user')
    flat = models.IntegerField(null=True)
    floor = models.IntegerField(null=True)
    people = models.IntegerField(null=True)
    car = models.BooleanField(default=False)
    car_model = models.CharField(max_length=128, default=None, null=True, blank=True)
    car_color = models.CharField(max_length=64, default=None, null=True, blank=True)


    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Все пользователи'

    def __str__(self):
        return '%s' % self.full_name
