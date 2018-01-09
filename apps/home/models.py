from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from apps.theater.models import Play


class Playbill(models.Model):
    """Модель афиши."""
    play = models.ForeignKey(
        Play,
        verbose_name='Спектакль'
    )
    image = ThumbnailerImageField(
        'Изображение',
        upload_to='home',
        help_text='Оптимальный размер: 1140px*590px.'
    )

    class Meta:
        verbose_name = 'Афиша главной страницы'
        verbose_name_plural = 'Афиша главной страницы'
