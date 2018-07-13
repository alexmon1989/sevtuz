from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


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
    month_from = models.PositiveIntegerField('Месяц с', choices=MONTHS_CHOICES, default=9)
    month_to = models.PositiveIntegerField('Месяц по', choices=MONTHS_CHOICES, default=5)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'
        ordering = ('year_from',)


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
        ordering = ('title',)


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
    has_page = models.BooleanField('Есть собственная страница', default=True)
    is_actor = models.BooleanField(
        'Является актёром',
        default=False,
        help_text="Если выбрано, то на странице персоны активным пунктом меню будет Труппа, "
                  "иначе - Художественная часть (если эти страницы существуют)."
    )
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность или звание')
    birthdate = models.DateField('Дата рождения', blank=True, null=True)
    education = models.CharField('Образование', max_length=255, blank=True, null=True)
    prizes = models.TextField('Награды', blank=True, null=True)
    ranks = models.TextField('Звания', blank=True, null=True)
    biography = RichTextUploadingField('Биография', blank=True, null=True)
    plays = RichTextUploadingField('Спектакли СевТЮЗа', blank=True, null=True)
    cinema = RichTextUploadingField('Роли в кино', blank=True, null=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('person_detail', args=[self.slug])

    def get_photos(self):
        """Возвращает список фотографий персоны."""
        return self.personphoto_set.filter(is_visible=True).order_by('created_at').all()

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'
        ordering = ('name',)


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
        ordering = ('title',)


class Play(models.Model):
    """Модель спектакля (представления)."""

    def upload_to(instance, filename):
        return 'plays/main-images/{}'.format(filename)

    title = models.CharField('Название', max_length=255)
    slug = models.SlugField(
        'Slug (для url)',
        max_length=255,
        default='',
        unique=True
    )
    age = models.PositiveIntegerField('Возраст зрителей, от')
    genre = models.ForeignKey(Genre, verbose_name='Жанр', on_delete=models.SET_NULL, null=True, blank=True)
    duration = models.DurationField('Продолжительность', null=True, blank=True, help_text='Используйте формат ЧЧ:ММ:СС')
    author = models.CharField('Автор', max_length=255, null=True, blank=True)
    staging = models.CharField('Инсценировка', max_length=255, null=True, blank=True)
    director = models.CharField('Режиссёр', max_length=255, null=True, blank=True)
    head_of_production = models.CharField('Руководитель постановки', max_length=255, null=True, blank=True)
    production_designer = models.CharField('Художник-постановщик', max_length=255, null=True, blank=True)
    lighting_designer = models.CharField('Художник по свету', max_length=255, null=True, blank=True)
    music = models.CharField('Музыкальное оформление', max_length=255, null=True, blank=True)
    choreographer = models.CharField('Хореограф', max_length=255, null=True, blank=True)
    text = RichTextUploadingField('Текст', null=True, blank=True)
    image = models.ImageField(
        'Основное изображение',
        upload_to=upload_to,
        null=True,
        blank=True,
        help_text='Оптимальный размер: 800px*500px.'
    )
    is_our_play = models.BooleanField('Спектакль нашего театра (отображать на странице "Спектакли")?', default=True)
    status = models.PositiveSmallIntegerField(
        'Статус спектакля',
        choices=(
            (1, 'Текущий'),
            (2, 'Архивный'),
            (3, 'Планируемый'),
        ),
        default=1
    )
    roles = models.ManyToManyField(Person, through='PersonPlayRole', related_name='roles', blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def get_events(self):
        """Возвращает 5 ближайших дат проведения спектакля."""
        return self.event_set.filter(is_visible=True, datetime__gte=timezone.now()).order_by('datetime').all()[:5]

    def get_photos(self):
        """Возвращает список фотографий спектакля."""
        return self.playphoto_set.filter(is_visible=True).order_by('created_at').all()

    def get_videos(self):
        """Возвращает список видео спектакля."""
        return self.playvideo_set.filter(is_visible=True).order_by('created_at').all()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('playbill_play_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Спектакль'
        verbose_name_plural = 'Спектакли'
        ordering = ('title',)


class PlayPhoto(models.Model):
    """Модель фотографии."""

    def upload_to(instance, filename):
        return 'plays/{}/{}'.format(instance.play.pk, filename)

    image = models.ImageField(
        'Изображение',
        upload_to=upload_to,
        help_text='Оптимальный размер: 800px*500px.'
    )
    play = models.ForeignKey(Play, on_delete=models.CASCADE, verbose_name='Спектакль')
    is_visible = models.BooleanField('Включено', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return 'Изображение #{}'.format(self.pk)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class PlayVideo(models.Model):
    """Модель видео спектакля."""
    youtube_id = models.CharField(
        'Идентификатор на Youtube',
        help_text='Например, для видео https://www.youtube.com/watch?v=JMJXvsCLu6, его идентификатором будет JMJXvsCLu6.',
        max_length=32
    )
    play = models.ForeignKey(Play, on_delete=models.CASCADE, verbose_name='Спектакль')
    is_visible = models.BooleanField('Включено', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return 'Видео #{}'.format(self.pk)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class PersonPlayRole(models.Model):
    """Модель для связи многие-ко-многим моделей Person и Play (роли)."""
    person = models.ForeignKey(Person, verbose_name='Актёр', on_delete=models.CASCADE)
    play = models.ForeignKey(Play, verbose_name='Спектакль', on_delete=models.CASCADE)
    role = models.CharField('Роль', max_length=255)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


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
        return reverse('theater_page', args=[self.slug])

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
        return reverse('theater_news_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-created_at',)


class History(models.Model):
    """Модель истории сезона."""
    season = models.OneToOneField(Season, verbose_name='Сезон', on_delete=models.CASCADE, blank=True, null=True)
    text = RichTextUploadingField('Текст', blank=False)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.season.title

    def get_absolute_url(self):
        return reverse('theater_history', args=[str(self.pk)])

    def get_photos(self):
        """Возвращает список фотографий истории сезона."""
        return self.historyphoto_set.filter(is_visible=True).order_by('created_at').all()

    def get_videos(self):
        """Возвращает список видео истории сезона."""
        return self.historyvideo_set.filter(is_visible=True).order_by('created_at').all()

    class Meta:
        verbose_name = 'История сезона'
        verbose_name_plural = 'История'
        ordering = ('season__year_from',)


class HistoryPhoto(models.Model):
    """Модель фотографии."""

    def upload_to(instance, filename):
        return 'histories/{}/{}'.format(instance.history.pk, filename)

    image = models.ImageField(
        'Изображение',
        upload_to=upload_to,
        help_text='Оптимальный размер: 800px*500px.'
    )
    history = models.ForeignKey(History, on_delete=models.CASCADE, verbose_name='Сезон')
    is_visible = models.BooleanField('Включено', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return 'Изображение #{}'.format(self.pk)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class HistoryVideo(models.Model):
    """Модель видео спектакля."""
    youtube_id = models.CharField(
        'Идентификатор на Youtube',
        help_text='Например, для видео https://www.youtube.com/watch?v=JMJXvsCLu6, его идентификатором будет JMJXvsCLu6.',
        max_length=32
    )
    history = models.ForeignKey(History, on_delete=models.CASCADE, verbose_name='Сезон')
    is_visible = models.BooleanField('Включено', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return 'Видео #{}'.format(self.pk)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class DocumentType(models.Model):
    """Модель типа документа."""
    title = models.CharField('Название', max_length=255)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    def get_documents(self):
        """Возвращает список документов типа."""
        return self.document_set.filter(is_visible=True).order_by('title').all()

    class Meta:
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Типы документов'


class Document(models.Model):
    """Модель документа."""
    title = models.CharField('Название', max_length=255)
    document_type = models.ForeignKey(DocumentType, verbose_name='Тип документа', on_delete=models.CASCADE)
    file = models.FileField('Файл', upload_to='documents/')
    is_visible = models.BooleanField('Включено', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ('title',)


class Partner(models.Model):
    """Модель партнёра."""
    title = models.CharField('Название', max_length=255)
    image = models.ImageField('Изображение', upload_to='partners/', help_text='Оптимальный размер, px: 200 х 100.')
    link = models.URLField('Ссылка', blank=True, null=True)
    is_visible = models.BooleanField('Включено', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'
