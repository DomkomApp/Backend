from django.db import models

from users.models import User


class House(models.Model):
    address = models.CharField(max_length=256)
    house_number = models.CharField(max_length=16)
    people = models.IntegerField()

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

    def __str__(self):
        return '%s %s' % (self.address, self.house_number)


class UsersInHouse(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    house = models.ForeignKey(House, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = 'Житель'
        verbose_name_plural = 'Все жители'

    def __str__(self):
        return '%s' % self.person
