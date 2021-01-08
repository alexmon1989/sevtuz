from django import template
from apps.media.models import Page

register = template.Library()


@register.simple_tag
def media_pages():
    """Возвращает список ссылок на статичные страницы приложения."""
    return Page.objects.filter(is_visible=True).order_by('-weight')
