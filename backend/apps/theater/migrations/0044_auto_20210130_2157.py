# Generated by Django 2.2.17 on 2021-01-30 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0043_auto_20210124_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='play_types',
            field=models.ManyToManyField(blank=True, to='theater.PlayType', verbose_name='Тип спектакля'),
        ),
    ]
