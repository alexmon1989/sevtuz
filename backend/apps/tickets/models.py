from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Page(models.Model):
    """Модель страницы."""
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField(
        'Slug (для url)',
        max_length=255,
        default='',
        unique=True
    )
    text = RichTextUploadingField('Текст', blank=False)
    is_visible = models.BooleanField('Включено', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tickets_page', args=[self.slug])

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = ('created_at',)
