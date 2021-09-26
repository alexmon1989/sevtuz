# Generated by Django 2.0.7 on 2018-08-19 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playbill', '0002_event_radario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='radario_id',
            field=models.IntegerField(blank=True, help_text='Например у события https://radario.ru/company/ticket-desk/events/280450 ID будет равен 280450.', null=True, verbose_name='ID события в системе Radario'),
        ),
    ]