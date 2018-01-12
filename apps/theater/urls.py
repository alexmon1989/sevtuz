from django.conf.urls import url
from apps.theater.views import (PageDetailView, NewsDetailView, NewsListView, HistoryDetailView, DocumentTypeListView,
                                PartnersListView, pages_list)

urlpatterns = [
    url(r'^$', pages_list, name='theater_pages'),
    url(r'^news/$', NewsListView.as_view(), name='theater_news_list'),
    url(r'^news/(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='theater_news_detail'),
    url(r'^history/$', HistoryDetailView.as_view(), name='theater_history'),
    url(r'^history/(?P<pk>\d+)/$', HistoryDetailView.as_view(), name='theater_history'),
    url(r'^documents/$', DocumentTypeListView.as_view(), name='theater_documents'),
    url(r'^partners/$', PartnersListView.as_view(), name='theater_partners'),
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='theater_page'),
]
