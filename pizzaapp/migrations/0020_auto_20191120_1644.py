# Generated by Django 2.2.7 on 2019-11-20 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0019_auto_20191120_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
