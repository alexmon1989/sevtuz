from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from apps.settings.models import FooterSettings, SocialLinksModel, HeaderSettings
from apps.settings.models import Analytics

register = template.Library()


@register.filter
def in_list(value, the_list):
    value = str(value)
    return value in the_list.split(',')


@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()


@register.filter()
def to_int(value):
    return int(value)


@register.filter
def duration(td):
    if td:
        total_seconds = int(td.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        return '{} час. {} мин.'.format(hours, minutes)
    return ''


@register.filter
def month_title(month_num):
    months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
              'Декабрь',)
    return months[month_num - 1]


@register.inclusion_tag('_partial/footer_2.html')
def footer_2():
    return {
        'footer_data': FooterSettings.objects.first(),
    }


@register.simple_tag
def social_links():
    return SocialLinksModel.objects.first()


@register.simple_tag
def analytics_code():
    """Возвращает HTML-код аналитики."""
    analytics, created = Analytics.objects.get_or_create()
    return mark_safe(analytics.code)


@register.simple_tag
def header_settings():
    """Возвращает настройки хедера."""
    print(123)
    obj, created = HeaderSettings.objects.get_or_create()
    return {
        'header_data': obj
    }
