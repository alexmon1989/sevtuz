# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-06 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20180105_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='template',
            field=models.SmallIntegerField(choices=[(1, '2 колонки, прямоугольные изображения'), (2, '3 колонки, круглые изображения')], default=1, verbose_name='Шаблон'),
        ),
    ]