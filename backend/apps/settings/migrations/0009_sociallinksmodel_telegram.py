# Generated by Django 2.2.17 on 2024-11-30 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0008_headersettings_ukgs_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallinksmodel',
            name='telegram',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Telegram'),
        ),
    ]
