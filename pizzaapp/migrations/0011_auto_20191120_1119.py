# Generated by Django 2.2.7 on 2019-11-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0010_auto_20191120_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='Toppings', to='pizzaapp.Toppings'),
        ),
    ]
