# Generated by Django 2.2.7 on 2019-11-27 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0030_auto_20191127_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='totalprice',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shop_cart',
            name='totalprice',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]