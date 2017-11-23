from django.conf.urls import url
from apps.plays.views import PlayListView

urlpatterns = [
    url(r'^current/$', PlayListView.as_view(), name='plays_list_current'),
    url(r'^archive/$', PlayListView.as_view(), name='plays_list_archive'),
    url(r'^plans/$', PlayListView.as_view(), name='plays_list_plans'),
]
