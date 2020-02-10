# Generated by Django 3.0.2 on 2020-01-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='grandtotal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderitems',
            field=models.ManyToManyField(blank=True, null=True, to='user.Cart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
