from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Office(models.Model):
    """Модель страницы Контора."""
    text = RichTextUploadingField('Текст', blank=False)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return 'Страница "Контора"'

    class Meta:
        verbose_name = 'Страница "Контора"'
        verbose_name_plural = 'Страница "Контора"'
