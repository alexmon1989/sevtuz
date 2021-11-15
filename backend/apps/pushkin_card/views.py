from django.shortcuts import render
from .models import Page


def index(request):
    page, created = Page.objects.get_or_create()
    return render(request, 'pushkin_card/index.html', {'page': page})
