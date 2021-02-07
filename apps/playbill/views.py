from django.views.generic import ListView, DetailView, TemplateView
from django.http import Http404
from django.utils.timezone import now
from django.db.models import Q
from django.db.models.functions import ExtractMonth
from django.shortcuts import render, redirect

from apps.theater.models import Play
from apps.playbill.models import Event


def pages_list(request):
    """Отображает страницу со списком сраниц приложения."""
    return render(request, 'playbill/page_list.html')


class PlayListView(ListView):
    """Отображает страницу со списком спектаклей театра."""
    model = Play
    template_name = 'playbill/plays/list/list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Если загружается страница текущих спектаклей, то необходимо получить возможные значения фильтров
        if self.request.resolver_match.url_name == 'playbill_plays_current':
            qs = Play.objects.filter(is_our_play=True, status=1)

            # Варианты возраста
            context['ages'] = list(set(qs.values_list('age', flat=True)))
            context['ages'].sort()

            # Варианты типов
            context['play_types'] = list(set(qs.filter(play_types__isnull=False).values_list(
                'play_types__pk', 'play_types__title'
            )))
            context['play_types'].sort()

        return context

    def get(self, *args, **kwargs):
        page = self.request.GET.get('page')
        if page:
            try:
                if int(page) == 1:
                    return redirect(self.request.resolver_match.url_name)
            except ValueError:
                raise Http404
        return super(PlayListView, self).get(*args, **kwargs)

    def get_queryset(self):
        qs = Play.objects.filter(is_our_play=True).order_by('created_at')

        full_path = self.request.get_full_path()

        statuses = ['current', 'archive', 'plans']
        for status in statuses:
            if status in full_path:
                qs = qs.filter(status=statuses.index(status)+1)

        # Фильтры
        if self.request.GET.get('age'):
            try:
                age = int(self.request.GET['age'])
                qs = qs.filter(age=age)
            except ValueError:
                raise Http404

        if self.request.GET.getlist('play_type'):
            qs = qs.filter(play_types__pk__in=self.request.GET.getlist('play_type'))

        return qs.distinct()


class PlayDetailView(DetailView):
    """Отображает страницу со спектаклем."""
    model = Play
    template_name = 'playbill/plays/detail/detail.html'

    def get(self, request, *args, **kwargs):
        # Синхронизация локальных событий и событий Радарио
        Event.fill_radario_ids()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['media_count'] = len(self.object.get_videos()) + len(self.object.get_photos())

        return context


class EventsListView(TemplateView):
    """Отображает страницу со спектаклями на плозадках театра."""
    template_name = 'playbill/events/list.html'

    def get(self, request, *args, **kwargs):
        # Синхронизация локальных событий и событий Радарио
        Event.fill_radario_ids()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Спектакли на наших площадках
        months = Event.objects.annotate(
            month=ExtractMonth('datetime')
        ).filter(
            is_visible=True, datetime__gte=now(), guests=False, tour=False, external=False
        ).values(
            'month'
        ).order_by(
            'month'
        ).distinct()

        context['events_our'] = []
        for month in months:
            context['events_our'].append(
                {
                    'month': month['month'],
                    'items': Event.objects.filter(
                        is_visible=True,
                        datetime__gte=now(),
                        datetime__month=month['month'],
                        guests=False,
                        tour=False,
                        external=False,
                    ).order_by('datetime').select_related('play', 'play__genre', 'scene'),
                }
            )

        # Наши гости
        context['events_guests'] = Event.objects.filter(
            is_visible=True, datetime__gte=now(), guests=True
        ).order_by('datetime').select_related('play', 'play__genre', 'scene')

        # Выезды и гастроли
        context['events_external_tour'] = Event.objects.filter(
            is_visible=True, datetime__gte=now()
        ).filter(
            Q(external=True) | Q(tour=True)
        ).order_by('datetime').select_related('play', 'play__genre', 'scene')

        return context
