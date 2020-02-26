from django.db import models

from authen.models import CustomUser

service_type = [
    ('RE','Ремонт'),
    ('TE','Пропуск'),
    ('SE','Доп Услуга')
]
status_type = [
    ('IN','В процессе'),
    ('RD','Выполнено')
]


class Service(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    service_type = models.CharField(choices=service_type,max_length=20)
    status = models.CharField(max_length=15,choices=status_type)
    description = models.TextField()

    def __str__(self):
        return self.service_type
