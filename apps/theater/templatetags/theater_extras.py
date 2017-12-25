from django import template
from apps.theater.models import News, Page

register = template.Library()


@register.simple_tag
def news_count(year, month):
    """Возвращает количество новостей в определённом месяце определённого года."""
    return News.objects.filter(created_at__year=year, created_at__month=month).count()


@register.simple_tag
def theater_pages():
    """Возвращает список ссылок на статичные страницы приложения."""
    return Page.objects.filter(is_visible=True).order_by('created_at').all()
