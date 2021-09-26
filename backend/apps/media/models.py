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
    text = RichTextUploadingField('Текст', blank=True)
    weight = models.PositiveSmallIntegerField(
        'Вес',
        default=1000,
        help_text='Чем больше значение, тем выше страница в списке.'
    )
    is_visible = models.BooleanField('Включено', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('media_page', args=[self.slug])

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = ('created_at',)


class News(models.Model):
    """Модель новости."""
    title = models.CharField('Заголовок', max_length=255, blank=False)
    slug = models.SlugField(
        'Slug (для url)',
        max_length=255,
        default='',
        unique=True
    )
    text = RichTextUploadingField('Текст', blank=False)
    is_visible = models.BooleanField('Включено', default=True)
    image = models.ImageField(
        'Изображение',
        upload_to='news',
        null=True,
        blank=True,
        help_text='Оптимальный размер: 800px*500px.'
    )
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('media_news_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-created_at',)