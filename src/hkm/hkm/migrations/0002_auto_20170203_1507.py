# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-03 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hkm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printproduct',
            name='prize',
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='total_prize',
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='unit_prize',
        ),
        migrations.AddField(
            model_name='printproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='productorder',
            name='datetime_payment_processed',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Payment processed at'),
        ),
        migrations.AddField(
            model_name='productorder',
            name='is_payment_successful',
            field=models.NullBooleanField(verbose_name='Payment successful'),
        ),
        migrations.AddField(
            model_name='productorder',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total price'),
        ),
        migrations.AddField(
            model_name='productorder',
            name='unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Unit price'),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='is_checkout_successful',
            field=models.NullBooleanField(verbose_name='Checkout successful'),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='is_order_successful',
            field=models.NullBooleanField(verbose_name='Order successful'),
        ),
    ]
