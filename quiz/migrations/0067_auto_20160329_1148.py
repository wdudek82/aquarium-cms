# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0066_auto_20160325_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]