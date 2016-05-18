# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 11:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aquarium', '0032_auto_20160325_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='tank_id',
            field=models.IntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]