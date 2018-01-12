from django.conf.urls import url
from apps.projects.views import PageDetailView, PageListView

urlpatterns = [
    url(r'^$', PageListView.as_view(), name='projects_pages'),
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='projects_page'),
]
