# Generated by Django 2.2.7 on 2019-11-26 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0026_item_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(),
        ),
    ]
