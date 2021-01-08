from django.conf.urls import url
from apps.theater.views import (PageDetailView, HistoryDetailView, DocumentTypeListView)

urlpatterns = [
    url(r'^history/$', HistoryDetailView.as_view(), name='theater_history'),
    url(r'^history/(?P<pk>\d+)/$', HistoryDetailView.as_view(), name='theater_history'),
    url(r'^documents/$', DocumentTypeListView.as_view(), name='theater_documents'),
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='theater_page'),
]
