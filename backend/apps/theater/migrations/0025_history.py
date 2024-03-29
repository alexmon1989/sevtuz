# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 15:51
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0024_auto_20171225_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('season', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='theater.Season', verbose_name='Сезон')),
            ],
            options={
                'verbose_name': 'Сезон',
                'verbose_name_plural': 'История',
            },
        ),
    ]
