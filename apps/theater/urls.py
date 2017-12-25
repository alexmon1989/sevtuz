from django.conf.urls import url
from apps.theater.views import PageDetailView, NewsDetailView, NewsListView, HistoryDetailView

urlpatterns = [
    url(r'^news/$', NewsListView.as_view(), name='theater_news_list'),
    url(r'^news/(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='theater_news_detail'),
    url(r'^history/$', HistoryDetailView.as_view(), name='theater_history'),
    url(r'^history/(?P<pk>\d+)/$', HistoryDetailView.as_view(), name='theater_history'),
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='theater_page'),
]
