from django.conf.urls import url
from apps.playbill.views import PlayListView, PlayDetailView, pages_list, EventsListView

urlpatterns = [
    url(r'^$', pages_list, name='playbill_pages'),
    url(r'^plays/current/$', PlayListView.as_view(), name='playbill_plays_current'),
    url(r'^plays/archive/$', PlayListView.as_view(), name='playbill_plays_archive'),
    url(r'^plays/plans/$', PlayListView.as_view(), name='playbill_plays_plans'),
    url(r'^plays/show/(?P<slug>[-\w]+)/$', PlayDetailView.as_view(), name='playbill_play_detail'),
    url(r'^events/$', EventsListView.as_view(), name='playbill_events_list'),
]
