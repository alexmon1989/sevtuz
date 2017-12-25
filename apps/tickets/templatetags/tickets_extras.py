from django import template
from apps.tickets.models import Page

register = template.Library()


@register.simple_tag
def tickets_pages():
    """Возвращает список ссылок на статичные страницы приложения."""
    return Page.objects.filter(is_visible=True).order_by('created_at').all()
