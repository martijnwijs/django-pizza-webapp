# Generated by Django 2.2.7 on 2019-11-20 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0007_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Toppings', to='pizzaapp.Toppings'),
            preserve_default=False,
        ),
    ]
