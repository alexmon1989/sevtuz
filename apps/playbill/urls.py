from django.conf.urls import url
from apps.playbill.views import PlayListView, PlayDetailView, events_list, get_events_table

urlpatterns = [
    url(r'^plays/current/$', PlayListView.as_view(), name='playbill_plays_current'),
    url(r'^plays/archive/$', PlayListView.as_view(), name='playbill_plays_archive'),
    url(r'^plays/plans/$', PlayListView.as_view(), name='playbill_plays_plans'),
    url(r'^plays/show/(?P<slug>[-\w]+)/$', PlayDetailView.as_view(), name='playbill_play_detail'),
    url(r'^events/$', events_list, name='playbill_events_list'),
    url(r'^events/get_events_table$', get_events_table, name='playbill_get_events_table'),
]
