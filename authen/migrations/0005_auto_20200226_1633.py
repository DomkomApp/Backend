# Generated by Django 3.0.3 on 2020-02-26 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0004_auto_20200226_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
