# Generated by Django 2.2.7 on 2019-11-20 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0021_auto_20191120_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Size_menu', to='pizzaapp.Size'),
        ),
    ]
