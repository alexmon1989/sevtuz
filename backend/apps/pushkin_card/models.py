from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Page(models.Model):
    """Модель страницы."""
    title = models.CharField('Заголовок', max_length=255, default='Пушкинская карта')
    text = RichTextUploadingField('Текст', blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = ('created_at',)
