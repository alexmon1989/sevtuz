from django.conf.urls import url
from apps.repertoire.views import events_list, get_events_table

urlpatterns = [
    url(r'^$', events_list, name='events_list'),
    url(r'^get_events_table$', get_events_table, name='get_events_table'),
]
