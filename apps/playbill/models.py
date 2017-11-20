from django.db import models
from apps.theater.models import Play


class Scene(models.Model):
    """Модель сцены."""
    title = models.CharField('Название', max_length=255)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сцена'
        verbose_name_plural = 'Сцены'


class Event(models.Model):
    """Модель события (представления)."""
    datetime = models.DateTimeField('Дата и время начала')
    play = models.ForeignKey(Play, verbose_name='Спектакль', on_delete=models.CASCADE)
    scene = models.ForeignKey(Scene, verbose_name='Сцена', on_delete=models.CASCADE)
    free_enter = models.BooleanField('Свободный вход', default=False)
    is_premiere = models.BooleanField('Премьера', default=False)
    gts = models.BooleanField('ГТС', default=False)
    tour = models.BooleanField('Гастроли', default=False)
    is_visible = models.BooleanField('Включено', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.play.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
