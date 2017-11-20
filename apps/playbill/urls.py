from django.conf.urls import url
from apps.playbill.views import EventListView

urlpatterns = [
    url(r'^$', EventListView.as_view(), name='events_list'),
]
