from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Season(models.Model):
    MONTHS_CHOICES = (
        (1, 'Январь'),
        (2, 'Февраль'),
        (3, 'Март'),
        (4, 'Апрель'),
        (5, 'Май'),
        (6, 'Июнь'),
        (7, 'Июль'),
        (8, 'Август'),
        (9, 'Сентябрь'),
        (10, 'Октябрь'),
        (11, 'Ноябрь'),
        (12, 'Декабрь'),
    )

    title = models.CharField('Название', max_length=255)
    year_from = models.PositiveIntegerField('Год с', default=None)
    year_to = models.PositiveIntegerField('Год по', default=None)
    month_from = models.PositiveIntegerField('Месяц с', choices=MONTHS_CHOICES, default=None)
    month_to = models.PositiveIntegerField('Месяц по', choices=MONTHS_CHOICES, default=None)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'


class Genre(models.Model):
    """Модель жанра."""
    title = models.CharField('Название', max_length=255)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Play(models.Model):
    """Модель спектакля (представления)."""
    def upload_to(instance, filename):
        return 'plays/main-images/{}'.format(filename)

    title = models.CharField('Название', max_length=255)
    age = models.PositiveIntegerField('Возраст зрителей, от')
    genre = models.ForeignKey(Genre, verbose_name='Жанр', on_delete=models.SET_NULL, null=True, blank=True)
    duration = models.DurationField('Продолжительность', null=True, blank=True, help_text='Используйте формат ЧЧ:ММ:СС')
    author = models.CharField('Автор', max_length=255, null=True, blank=True)
    staging = models.CharField('Инсценировка', max_length=255, null=True, blank=True)
    director = models.CharField('Режиссёр', max_length=255, null=True, blank=True)
    head_of_production = models.CharField('Руководитель постановки', max_length=255, null=True, blank=True)
    production_designer = models.CharField('Художник-постановщик', max_length=255, null=True, blank=True)
    lighting_designer = models.CharField('Художник по свету', max_length=255, null=True, blank=True)
    choreographer = models.CharField('Хореограф', max_length=255, null=True, blank=True)
    text = RichTextUploadingField('Текст', null=True, blank=True)
    image = models.ImageField(
        'Основное изображение',
        upload_to=upload_to,
        null=True,
        blank=True,
        help_text='Оптимальный размер: 740px*380px.'
    )
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Спектакль'
        verbose_name_plural = 'Спектакли'


class PlayPhoto(models.Model):
    """Модель фотографии."""
    def upload_to(instance, filename):
        return 'plays/{}/{}'.format(instance.play.pk, filename)

    image = models.ImageField('Изображение', upload_to=upload_to)
    play = models.ForeignKey(Play, on_delete=models.CASCADE, verbose_name='Спектакль')
    is_visible = models.BooleanField('Включено', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return 'Изображение #{}'.format(self.pk)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
