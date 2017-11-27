from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from apps.theater.models import Play


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
    persons = models.ManyToManyField('Person', verbose_name='Сотрудники', blank=True)
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


class Position(models.Model):
    """Модель должности."""
    title = models.CharField('Название', max_length=255)
    weight = models.PositiveIntegerField(
        'Вес',
        default=10000,
        help_text='Чем выше вес, тем "выше" сотрудник с этой должностью на странице.'
    )
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Person(models.Model):
    """Модель сотрудника театра."""
    name = models.CharField('ФИО', max_length=255)
    slug = models.SlugField(
        'Slug (для url)',
        max_length=255,
        default='',
        unique=True
    )
    image = models.ImageField(
        'Фото',
        upload_to='people/',
        null=True,
        blank=True,
        help_text='Оптимальный размер: 400px*550px.'
    )
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность')
    birthdate = models.DateField('Дата рождения', blank=True, null=True)
    education = models.CharField('Образование', max_length=255, blank=True, null=True)
    prizes = models.TextField('Награды', blank=True, null=True)
    ranks = models.TextField('Звания', blank=True, null=True)
    biography = RichTextUploadingField('Биография', blank=True, null=True)
    has_page = models.BooleanField('Есть собственная страница?', default=True)
    current_plays = models.ManyToManyField(Play, through='CurrentPlay', related_name='current_plays', blank=True)
    last_plays = models.ManyToManyField(Play, through='LastPlay', related_name='last_plays', blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.name

    def get_photos(self):
        """Возвращает список фотографий сотрудника."""
        return self.personphoto_set.filter(is_visible=True).order_by('created_at').all()

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class PersonPhoto(models.Model):
    """Модель фотографии."""

    def upload_to(instance, filename):
        return 'people/{}/{}'.format(instance.person.pk, filename)

    image = models.ImageField(
        'Изображение',
        upload_to=upload_to,
        help_text='Оптимальный размер: 800px*500px.'
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Сотрудник')
    is_visible = models.BooleanField('Включено', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return 'Изображение #{}'.format(self.pk)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Галерея'


class CurrentPlay(models.Model):
    """Модель для связи многие-ко-многим моделей Person и Play (текущие спектакли)."""
    person = models.ForeignKey(Person)
    play = models.ForeignKey(Play, verbose_name='Спектакль')
    text = models.CharField('Текст', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Спектакль'
        verbose_name_plural = 'Текущие спектакли'


class LastPlay(models.Model):
    """Модель для связи многие-ко-многим моделей Person и Play (спектакли прошлых лет)."""
    person = models.ForeignKey(Person)
    play = models.ForeignKey(Play, verbose_name='Спектакль')
    text = models.CharField('Текст', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Спектакль'
        verbose_name_plural = 'Спектакли прошлых лет'
