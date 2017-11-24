from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Page(models.Model):
    """Модель страницы."""
    text = RichTextUploadingField('Текст', blank=False)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return 'Страница "Контакты"'

    class Meta:
        verbose_name = 'Данные страницы'
        verbose_name_plural = 'Данные страницы'
