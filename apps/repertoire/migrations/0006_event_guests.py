# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repertoire', '0005_event_external'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='guests',
            field=models.BooleanField(default=False, verbose_name='Наши гости / к нам едут'),
        ),
    ]