# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0013_playvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playvideo',
            name='youtube_id',
            field=models.CharField(help_text='Например, для видео https://www.youtube.com/watch?v=ZyMByVSIEKE, его идентификатором будет ZyMByVSIEKE.', max_length=32, verbose_name='Идентификатор на Youtube'),
        ),
    ]