from django.conf.urls import url
from apps.media.views import PageDetailView, PageListView

urlpatterns = [
    url(r'^$', PageListView.as_view(), name='media_pages'),
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='media_page'),
]
