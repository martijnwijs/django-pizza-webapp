# Generated by Django 2.2.7 on 2019-11-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0035_order_delivered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='name',
            name='type',
        ),
        migrations.AddField(
            model_name='name',
            name='type',
            field=models.ManyToManyField(blank=True, null=True, related_name='Typename', to='pizzaapp.Type'),
        ),
    ]
