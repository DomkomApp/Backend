# Generated by Django 3.0.3 on 2020-03-11 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housereg', '0007_auto_20200310_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersinhouse',
            old_name='people',
            new_name='people_count',
        ),
    ]