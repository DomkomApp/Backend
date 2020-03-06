from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User
from authen.models import CustomUser


class House(models.Model):
    address = models.CharField(max_length=256)
    house_number = models.CharField(max_length=16)
    people = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

    def __str__(self):
        return '%s %s' % (self.address, self.house_number)


class UsersInHouse(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None, related_name='person')
    house = models.ForeignKey(House, on_delete=models.CASCADE, default=None)
    people = models.IntegerField(default=None)

    class Meta:
        verbose_name = 'Житель'
        verbose_name_plural = 'Все жители'

    def __str__(self):
        return '%s' % self.person


@receiver(post_save, sender=UsersInHouse)
def persons_count(sender, instance, created, **kwargs):
    users, created = House.objects.get_or_create()
    users.people += instance.people
    print(users.people)
    users.save()
