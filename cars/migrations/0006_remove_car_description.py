# Generated by Django 4.2.6 on 2023-10-19 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_doors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='description',
        ),
    ]
