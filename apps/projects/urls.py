from django.conf.urls import url
from apps.projects.views import PageDetailView

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='projects_page'),
]
