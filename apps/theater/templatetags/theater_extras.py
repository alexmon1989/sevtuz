from django import template
from apps.theater.models import News

register = template.Library()


@register.simple_tag
def news_count(year, month):
    """Возвращает количество новостей в определённом месяце определённого года."""
    return News.objects.filter(created_at__year=year, created_at__month=month).count()
