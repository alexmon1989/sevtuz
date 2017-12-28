from django.views.generic import ListView, DetailView
from django.http import Http404

from apps.theater.models import Play
from django.shortcuts import render, redirect
from apps.playbill.models import Event, Scene
from datetime import datetime
from django.urls import reverse

import re


class PlayListView(ListView):
    """Отображает страницу со списком спектаклей театра."""
    model = Play
    template_name = 'playbill/plays/list/list.html'
    paginate_by = 10

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

        return qs


class PlayDetailView(DetailView):
    """Отображает страницу со спектаклем."""
    model = Play
    template_name = 'playbill/plays/detail/detail.html'


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
