import json
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import modelform_factory
from django.db.models import Q
from apps.theater.models import InternalEvent
from apps.playbill.models import Event as ExternalEvent
from .models import Office
from datetime import timedelta
from pybb import util


def is_theater_employee(user):
    """Проверяет является ли пользователь сотрудником театра."""
    try:
        if user.person:
            return True
    except User.person.RelatedObjectDoesNotExist:
        return False


@login_required
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
            is_visible=True
        ).filter(
            Q(participants__in=(request.user.person,)) | Q(show_for_all=True)
        ).prefetch_related('participants').distinct()
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
            is_visible=True
        ).filter(
            Q(participants__in=(request.user.person,)) | Q(show_for_all=True)
        ).prefetch_related('participants').distinct()
    ]

    internal_events.extend(external_events)
    return render(request, 'staff_office/calendar/index.html', {
        'events': json.dumps(internal_events)
    })


@login_required
@user_passes_test(is_theater_employee)
def office(request):
    """Отображает страницу Контора."""
    page, created = Office.objects.get_or_create(defaults={'text': ''})
    return render(request, 'staff_office/office/index.html', {'page': page})


@login_required
@user_passes_test(is_theater_employee)
def profile(request):
    """Отображает страницу редактирования данных профиля."""
    UserForm = modelform_factory(User, fields=("username", "email"))
    PybbForm = modelform_factory(util.get_pybb_profile_model(), fields=("avatar",))

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        pybb_form = PybbForm(request.POST, request.FILES, instance=request.user.pybb_profile)
        if user_form.is_valid() and pybb_form.is_valid():
            user_form.save()
            pybb_form.save()
            messages.add_message(request, messages.SUCCESS, 'Ваши данные успешно сохранены.')
            return redirect(reverse('staff_office_profile'))
    else:
        user_form = UserForm(instance=request.user)
        pybb_form = PybbForm(instance=request.user.pybb_profile)

    return render(request, 'staff_office/profile/index.html', {
        'user_form': user_form,
        'pybb_form': pybb_form,
    })
