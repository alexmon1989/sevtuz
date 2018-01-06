from django.conf.urls import url
from apps.media.views import PageDetailView

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='media_page'),
]
