# Generated by Django 2.2.17 on 2021-09-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playbill', '0006_event_html_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_pushkin',
            field=models.BooleanField(default=False, verbose_name='Участник программы "Пушкинская карта"'),
        ),
    ]
