# Generated by Django 3.0.2 on 2020-01-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_auto_20200129_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.IntegerField(default=0),
        ),
    ]
