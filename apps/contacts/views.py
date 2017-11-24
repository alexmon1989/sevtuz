from django.shortcuts import render
from apps.contacts.models import Page


def page_detail(request):
    """Отображает страницу Контакты."""
    page, created = Page.objects.get_or_create(defaults={'text': ''})
    return render(request, 'contacts/page_details.html', {'page': page})
