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


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Введите телефон.")

        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            password=password,
            username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
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
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Все пользователи'

    def __str__(self):
        return '%s' % self.full_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True