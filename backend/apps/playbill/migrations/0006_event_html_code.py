# Generated by Django 2.2.17 on 2021-01-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playbill', '0005_event_show_for_all'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='html_code',
            field=models.TextField(blank=True, help_text='HTML-код отображаемый на вкладке "Выезды и гастроли" на месте кнопки "Купить билет"', null=True, verbose_name='HTML-код'),
        ),
    ]
