# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playbill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='free_enter',
            field=models.BooleanField(default=False, verbose_name='Свободный вход'),
        ),
        migrations.AddField(
            model_name='event',
            name='gts',
            field=models.BooleanField(default=False, verbose_name='ГТС'),
        ),
        migrations.AddField(
            model_name='event',
            name='is_premiere',
            field=models.BooleanField(default=False, verbose_name='Премьера'),
        ),
        migrations.AddField(
            model_name='event',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name='Включено'),
        ),
        migrations.AddField(
            model_name='event',
            name='tour',
            field=models.BooleanField(default=False, verbose_name='Гастроли'),
        ),
        migrations.AddField(
            model_name='event',
            name='scene',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='playbill.Scene', verbose_name='Сцена'),
            preserve_default=False,
        ),
    ]
