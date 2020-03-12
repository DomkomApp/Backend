from django.db import models
from authen.models import CustomUser


class OwnerType(models.Model):
    user_type = models.CharField(verbose_name='Тип владельца', max_length=64)

    class Meta:
        verbose_name = 'Тип владельца'
        verbose_name_plural = 'Типы владельцев'

    def __str__(self):
        return self.user_type


class Car(models.Model):
    owner = models.ForeignKey('User', verbose_name='Владелец', on_delete=models.CASCADE, default=None, null=True, blank=True,
                              related_name='automobile')
    car_brand = models.CharField(verbose_name='Бренд', max_length=64)
    car_model = models.CharField(verbose_name='Модель', max_length=64)
    car_number = models.CharField(verbose_name='Номер', max_length=64)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return '%s %s %s' % (self.car_brand, self.car_model, self.car_number)


class User(models.Model):
    phone = models.OneToOneField(CustomUser, verbose_name='Телефон', on_delete=models.CASCADE, related_name='user_profile')
    full_name = models.CharField(verbose_name='Ф.И.О.', max_length=128, null=False, blank=False)
    address = models.CharField(verbose_name='Адрес', max_length=128)
    owner_type = models.ForeignKey(OwnerType, verbose_name='Тип владельца', on_delete=models.CASCADE, default=None, null=True,
                                   related_name='owner_user')
    flat = models.IntegerField(verbose_name='Номер квартиры', null=True)
    floor = models.IntegerField(verbose_name='Этаж', null=True)
    people = models.IntegerField(verbose_name='Кол-во жителей', null=True)

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Все пользователи'

    def __str__(self):
        return '%s' % self.full_name
