from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin
from .managers import *
# Create your models here.
from django.contrib.auth.models import UserManager


class CustomUser(AbstractBaseUser):
    phone = models.CharField(verbose_name='Номер телефона',unique=True,max_length=15)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        verbose_name = 'Регистрация номера'
        verbose_name_plural = 'Регистрация номеров'
