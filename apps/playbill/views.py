from django.views.generic import ListView, DetailView
from django.http import Http404

from apps.theater.models import Play
from django.shortcuts import render, redirect
from apps.playbill.models import Event, Scene
from datetime import datetime
from django.urls import reverse

import re


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


def events_list(request):
    """Отображает страницу со списком событий."""
    date_now = datetime.now()
    month = int(request.GET.get('month', date_now.month))
    year = int(request.GET.get('year', date_now.year))

    if request.GET and year == date_now.year and month == date_now.month:
        return redirect(reverse('playbill_events_list'))

    # Предыдущие и следующие месяц, год
    prev_month = month - 1
    prev_year = year
    if prev_month == 0:
        prev_month, prev_year = 12, prev_year - 1
    elif prev_month == 12:
        prev_month, prev_year = 1, prev_year + 1
    next_month = month + 1
    next_year = year
    if next_month == 13:
        next_month, next_year = 1, next_year + 1
    elif prev_month == 0:
        next_month, next_year = 12, next_year - 1

    # Сцены для вывода в фильтре
    scenes = Scene.objects.filter(show_in_filter=True).order_by('title')

    # Синхронизация локальных событий и событий Радарио
    Event.fill_radario_ids()

    return render(
        request,
        'playbill/repertoire/list.html',
        {
            'current_year': date_now.year,
            'month': month,
            'year': year,
            'prev_month': prev_month,
            'prev_year': prev_year,
            'next_month': next_month,
            'next_year': next_year,
            'scenes': scenes
        }
    )


def get_events_table(request):
    """Возвращает HTML с таблицей отфильтрованных событий."""
    date_now = datetime.now()
    month = request.GET.get('month', date_now.month) or date_now.month
    year = request.GET.get('year', date_now.year) or date_now.year
    event_list = Event.objects.filter(is_visible=True, datetime__month=month, datetime__year=year).order_by('datetime')

    # Фильтра
    filter_1_value = request.GET.get('filter1')
    filter_2_value = request.GET.get('filter2')

    if re.search('scene_\d+', filter_1_value):
        event_list = event_list.filter(scene=re.findall('\d+', filter_1_value)[0])
    elif filter_1_value == 'external':
        event_list = event_list.filter(external=True)
    elif filter_1_value == 'tour':
        event_list = event_list.filter(tour=True)
    elif filter_1_value == 'gts':
        event_list = event_list.filter(gts=True)
    elif filter_1_value == 'guests':
        event_list = event_list.filter(guests=True)

    if filter_2_value == 'adults':
        event_list = event_list.filter(play__age__gte=14)

    return render(
        request,
        'playbill/repertoire/_partial/list_table.html',
        {
            'event_list': event_list,
        }
    )
