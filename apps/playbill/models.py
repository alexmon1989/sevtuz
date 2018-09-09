from django.db import models
from apps.theater.models import Play
from django.utils import timezone
from apps.playbill.utils import get_radario_events
import datetime
import dateutil.parser
from apps.theater.models import Person


class Scene(models.Model):
    """Модель сцены."""
    title = models.CharField('Название', max_length=255)
    show_in_filter = models.BooleanField(
        'Показывать в фильтре',
        default=False,
        help_text='Показывать в фильтре на странице "Репертуар"'
    )
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сцена'
        verbose_name_plural = 'Сцены'


class Event(models.Model):
    """Модель события (представления)."""
    datetime = models.DateTimeField('Дата и время начала')
    play = models.ForeignKey(Play, verbose_name='Спектакль', on_delete=models.CASCADE)
    scene = models.ForeignKey(Scene, verbose_name='Сцена', on_delete=models.CASCADE)
    participants = models.ManyToManyField(Person, verbose_name='Участники', blank=True)
    free_enter = models.BooleanField('Свободный вход', default=False)
    is_premiere = models.BooleanField('Премьера', default=False)
    gts = models.BooleanField('ГТС', default=False)
    external = models.BooleanField('Выездной спектакль', default=False)
    tour = models.BooleanField('Гастроли', default=False)
    guests = models.BooleanField('Наши гости / к нам едут', default=False)
    show_for_all = models.BooleanField('Показывать всем в служебном кабинете?', default=False)
    radario_id = models.IntegerField(
        'ID события в системе Radario',
        null=True,
        blank=True,
        help_text='Например у события https://radario.ru/company/ticket-desk/events/280450 ID будет равен 280450.'
    )
    is_visible = models.BooleanField('Включено', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.play.title

    @staticmethod
    def fill_radario_ids():
        """Заполняет radario_id у событий где его нет."""
        future_events = Event.objects.filter(
            is_visible=True,
            radario_id__isnull=True,
            datetime__gte=datetime.datetime.today()
        )
        if len(future_events) > 0:
            radario_events = get_radario_events()
            if radario_events and radario_events['success'] and radario_events['data']['totalCount'] > 0:
                for fevent in future_events:
                    for revent in radario_events['data']['items']:
                        # Если у локальных событий с радарио сходятся дата начала и название - это одно и то же событие
                        if (fevent.datetime == dateutil.parser.parse(revent['beginDate'])
                                and fevent.play.title == revent['title']):
                            fevent.radario_id = revent['id']
                            fevent.save()

    @property
    def is_past_due(self):
        return timezone.now() > self.datetime

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
