from django.conf.urls import url
from apps.theater.views import PageDetailView

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='theater_page'),
]
