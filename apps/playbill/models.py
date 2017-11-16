from django.db import models


class Event(models.Model):
    """Модель события (представления)."""
    datetime = models.DateTimeField('Дата и время начала')
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
