# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 10:53
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20180105_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationspage',
            name='hr_contacts',
            field=ckeditor.fields.RichTextField(verbose_name='Текст контактов специалиста по кадрам'),
        ),
    ]
