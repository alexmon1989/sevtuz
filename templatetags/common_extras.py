from django import template
from django.conf import settings
from django.utils import timezone
from apps.settings.models import FooterSettings, SocialLinksModel
from apps.repertoire.models import Event
from apps.theater.models import Page

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
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    return '{} час. {} мин.'.format(hours, minutes)


@register.filter
def month_title(month_num):
    months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
              'Декабрь',)
    return months[month_num - 1]


@register.inclusion_tag('_partial/footer_1.html')
def footer_1():
    return {
        'footer_data': FooterSettings.objects.first(),
        'last_events': Event.objects.filter(is_visible=True, datetime__gte=timezone.now()).order_by('datetime')[:3]
    }


@register.simple_tag
def social_links():
    return SocialLinksModel.objects.first()


@register.simple_tag
def theater_submenu():
    return Page.objects.filter(is_visible=True).order_by('created_at')
