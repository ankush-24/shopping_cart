# Generated by Django 3.0.2 on 2020-01-13 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200108_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]