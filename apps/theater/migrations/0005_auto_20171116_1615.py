# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 14:15
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0004_play_playphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст'),
        ),
    ]
