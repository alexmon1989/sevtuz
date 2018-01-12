from django.conf.urls import url
from apps.tickets.views import PageDetailView, PageListView

urlpatterns = [
    url(r'^$', PageListView.as_view(), name='tickets_pages'),
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='tickets_page'),
]
