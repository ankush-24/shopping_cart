# Generated by Django 3.0.2 on 2020-01-15 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200115_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total_price',
        ),
    ]
