# Generated by Django 2.2.7 on 2019-11-20 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0016_auto_20191120_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='extracheese',
        ),
    ]
