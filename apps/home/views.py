from django.shortcuts import render
from apps.news.models import News


def home(request):
    """Отображает главную страницу сайта."""
    last_news = News.objects.filter(is_visible=True).order_by('-created_at')[:3]
    return render(
        request,
        'home/index.html',
        {
            'last_news': last_news
        }
    )
