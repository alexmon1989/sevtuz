from django.db import models
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField
from apps.repertoire.models import Event


def limit_event_choices():
    return {'datetime__gte': timezone.now()}


class MainEvent(models.Model):
    """Модель анонса главного события."""
    event = models.ForeignKey(
        Event,
        verbose_name='Событие',
        limit_choices_to=limit_event_choices,
        help_text='Здесь показаны только будущие события'
    )
    image = ThumbnailerImageField(
        'Изображение',
        upload_to='home',
        help_text='Оптимальный размер: 1140px*590px.'
    )

    class Meta:
        verbose_name = 'Главное событие'
        verbose_name_plural = 'Главное событие'
