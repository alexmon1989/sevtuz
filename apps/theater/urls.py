from django.conf.urls import url
from apps.theater.views import PageDetailView, NewsDetailView, NewsListView

urlpatterns = [
    url(r'^news/$', NewsListView.as_view(), name='theater_news_list'),
    url(r'^news/(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='theater_news_detail'),
    url(r'^page/(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='theater_page'),
]
