# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-29 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0006_auto_20200614_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product_list',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
