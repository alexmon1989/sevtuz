# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 13:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20171123_1500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playbill',
            options={'verbose_name': 'Афиша главного события', 'verbose_name_plural': 'Афиша главного события'},
        ),
    ]
