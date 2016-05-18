# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aquarium', '0008_remove_tank_grades'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text_eng', models.TextField()),
                ('text_arabic', models.TextField()),
                ('habitat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aquarium.Habitat')),
            ],
        ),
    ]