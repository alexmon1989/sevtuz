from django.shortcuts import render
from apps.tickets.models import Page


def page_detail(request):
    """Отображает страницу Билеты."""
    page, created = Page.objects.get_or_create(defaults={'text': ''})
    return render(request, 'tickets/page_details.html', {'page': page})
