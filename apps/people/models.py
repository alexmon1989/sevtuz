from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from apps.theater.models import Play, Person


class Page(models.Model):
    """Модель страницы."""
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField(
        'Slug (для url)',
        max_length=255,
        default='',
        unique=True
    )
    text = RichTextUploadingField('Текст', blank=True, null=True)
    persons = models.ManyToManyField(Person, verbose_name='Сотрудники', blank=True)
    template = models.SmallIntegerField(
        'Шаблон',
        default=1,
        choices=(
            (1, '2 колонки, прямоугольные изображения'),
            (2, '3 колонки, круглые изображения'),
        )
    )
    is_visible = models.BooleanField('Включено', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('people_page', args=[self.slug])

    def get_persons(self):
        """Возвращает список отсортированных по весу должности сотрудников, относящихся к данной странице."""
        return self.persons.order_by('-position__weight', 'name')

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = ('created_at',)
