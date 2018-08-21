import json
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.utils import timezone
from apps.theater.models import InternalEvent
from apps.playbill.models import Event as ExternalEvent
from datetime import timedelta


def is_theater_employee(user):
    """Проверяет является ли пользователь сотрудником театра."""
    try:
        if user.person:
            return True
    except User.person.RelatedObjectDoesNotExist:
        return False


@user_passes_test(is_theater_employee)
def calendar(request):
    """Отображает страницу календаря событий сотрудника."""
    # Получение внутренних событий сотрудника
    internal_events = [
        {
            'title': e.title,
            'type': e.type,
            'start': e.start.strftime("%Y-%m-%d %H:%M:%S"),
            'end': e.end.strftime("%Y-%m-%d %H:%M:%S"),
            'responsible_person': e.responsible_person.name,
            'is_important': e.is_important,
            'participants': ', '.join([p.name for p in e.participants.all()]),
            'color': ('#AD4350' if e.is_important else '#3a87ad') if e.start >= timezone.now() else '#D1D1D1'
        }
        for e in InternalEvent.objects.filter(
            is_visible=True, participants__in=(request.user.person,)
        ).prefetch_related('participants')
    ]

    # Получение внешних событий сотрудника
    external_events = [
        {
            'title': e.play.title,
            'start': e.datetime.strftime("%Y-%m-%d %H:%M:%S"),
            'end': (e.datetime + timedelta(seconds=e.play.duration.seconds)).strftime("%Y-%m-%d %H:%M:%S"),
            'scene': e.scene.title,
            'is_important': True,
            'participants': ', '.join([p.name for p in e.participants.all()]),
            'color': '#AD4350' if e.datetime >= timezone.now() else '#D1D1D1'
        }
        for e in ExternalEvent.objects.filter(
            is_visible=True, participants__in=(request.user.person,)
        ).prefetch_related('participants')
    ]

    internal_events.extend(external_events)
    return render(request, 'staff_office/calendar/index.html', {
        'events': json.dumps(internal_events)
    })
