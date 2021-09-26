from django.conf.urls import url
from apps.media.views import PageDetailView, NewsDetailView, NewsListView

urlpatterns = [
    url(r'^news/$', NewsListView.as_view(), name='media_news_list'),
    url(r'^news/(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='media_news_detail'),
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='media_page'),
]
