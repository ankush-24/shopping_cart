# Generated by Django 3.0.2 on 2020-01-20 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200120_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='grandtotal',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]
