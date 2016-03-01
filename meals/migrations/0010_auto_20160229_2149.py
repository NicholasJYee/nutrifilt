# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0009_recipe_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(blank=True, default='g', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit_conversion_factor',
            field=models.FloatField(blank=True, default=1.0, null=True),
        ),
    ]
