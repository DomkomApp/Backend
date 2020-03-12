from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from authen.models import CustomUser


class House(models.Model):
    address = models.CharField(verbose_name='Адрес', max_length=256)
    house_number = models.CharField(verbose_name='Номер дома', max_length=16)
    people = models.IntegerField(verbose_name='Кол-во жителей', default=0, blank=True, null=True)

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

    def __str__(self):
        return '%s %s' % (self.address, self.house_number)


class UsersInHouse(models.Model):
    person = models.ForeignKey(CustomUser, verbose_name='Житель', on_delete=models.CASCADE, default=None, related_name='person')
    house = models.ForeignKey(House, verbose_name='Дом', on_delete=models.CASCADE, default=None)
    people_count = models.IntegerField(verbose_name='Кол-во жителей', default=None)

    class Meta:
        verbose_name = 'Житель'
        verbose_name_plural = 'Все жители'

    def __str__(self):
        return '%s' % self.person


@receiver(post_save, sender=UsersInHouse)
def persons_count(sender, instance, created, **kwargs):
    instance.house.people += instance.people_count
    instance.house.save()
