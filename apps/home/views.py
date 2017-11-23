from django.shortcuts import render
from django.utils import timezone
from apps.news.models import News
from apps.repertoire.models import Event
from apps.home.models import Playbill


def home(request):
    """Отображает главную страницу сайта."""
    last_news = News.objects.filter(is_visible=True).order_by('-created_at')[:3]
    last_events = Event.objects.filter(is_visible=True, datetime__gte=timezone.now()).order_by('datetime')[:10]
    playbill = Playbill.objects.first()
    return render(
        request,
        'home/index.html',
        {
            'last_news': last_news,
            'last_events': last_events,
            'main_event': playbill
        }
    )
