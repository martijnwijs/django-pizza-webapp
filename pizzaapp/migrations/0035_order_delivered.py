# Generated by Django 2.2.7 on 2019-11-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0034_remove_order_delivered'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
