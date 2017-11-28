from django.shortcuts import render, redirect
from apps.repertoire.models import Event
from datetime import datetime
from django.urls import reverse


def events_list(request):
    """Отображает страницу со списком событий."""
    date_now = datetime.now()
    month = int(request.GET.get('month', date_now.month))
    year = int(request.GET.get('year', date_now.year))

    if request.GET and year == date_now.year and month == date_now.month:
        return redirect(reverse('events_list'))

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

    return render(
        request,
        'repertoire/events/list.html',
        {
            'current_year': date_now.year,
            'month': month,
            'year': year,
            'prev_month': prev_month,
            'prev_year': prev_year,
            'next_month': next_month,
            'next_year': next_year,
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

    if filter_1_value == 'main_scene':
        event_list = event_list.filter(scene=1)
    elif filter_1_value == 'b_morskaya':
        event_list = event_list.filter(scene=2)
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
        'repertoire/events/_partial/list_table.html',
        {
            'event_list': event_list,
        }
    )
