# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-09 20:38
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20180107_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст'),
        ),
    ]
