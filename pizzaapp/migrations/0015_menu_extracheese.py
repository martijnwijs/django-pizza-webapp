# Generated by Django 2.2.7 on 2019-11-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0014_auto_20191120_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='extracheese',
            field=models.BooleanField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
