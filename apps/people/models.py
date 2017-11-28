from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
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
    text = RichTextUploadingField('Текст', blank=False)
    persons = models.ManyToManyField(Person, verbose_name='Сотрудники', blank=True)
    is_visible = models.BooleanField('Включено', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    def get_persons(self):
        """Возвращает список отсортированных по весу должности сотрудников, относящихся к данной странице."""
        return self.persons.order_by('-position__weight', 'name')

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


