from django.conf.urls import url
from apps.people.views import PageDetailView, PersonDetailView

urlpatterns = [
    url(r'^person/(?P<slug>[-\w]+)/$', PersonDetailView.as_view(), name='person_detail'),
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='people_page'),
]
