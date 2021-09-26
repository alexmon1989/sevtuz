# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0028_auto_20171226_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Персона', 'verbose_name_plural': 'Персоны'},
        ),
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.ImageField(help_text='Оптимальный размер, px: 200 х 100.', upload_to='partners/', verbose_name='Изображение'),
        ),
    ]