from django import template
from django.conf import settings

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

