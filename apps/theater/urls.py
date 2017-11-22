from django.conf.urls import url
from apps.theater.views import PlayDetailView

urlpatterns = [
    url(r'^play/(?P<slug>[-\w]+)/$', PlayDetailView.as_view(), name='play_detail'),
]
