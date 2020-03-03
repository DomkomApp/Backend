from django.db import models
from authen.models import CustomUser


class OwnerType(models.Model):
    user_type = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Тип владельца'
        verbose_name_plural = 'Типы владельцев'

    def __str__(self):
        return self.user_type


class Car(models.Model):
    owner = models.ForeignKey('User', on_delete=models.CASCADE, default=None, null=True, blank=True,
                              related_name='automobile')
    car_brand = models.CharField(max_length=64)
    car_model = models.CharField(max_length=64)
    car_number = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return '%s %s %s' % (self.car_brand, self.car_model, self.car_number)


class User(models.Model):
    phone = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_profile')
    full_name = models.CharField(max_length=128, null=False, blank=False)
    address = models.CharField(max_length=128)
    owner_type = models.ForeignKey(OwnerType, on_delete=models.CASCADE, default=None, null=True,
                                   related_name='owner_user')
    flat = models.IntegerField(null=True)
    floor = models.IntegerField(null=True)
    people = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Все пользователи'

    def __str__(self):
        return '%s' % self.full_name
