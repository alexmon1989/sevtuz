# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_analytics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footersettings',
            name='contacts_block_html',
        ),
        migrations.RemoveField(
            model_name='footersettings',
            name='information_block_title',
        ),
        migrations.AddField(
            model_name='footersettings',
            name='phone',
            field=models.TextField(blank=True, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='footersettings',
            name='information_block_text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст (html)'),
        ),
    ]
