from django.conf.urls import url
from apps.people.views import PageDetailView, PersonDetailView, VacanciesPageDetailView

urlpatterns = [
    url(r'^person/(?P<slug>[-\w]+)/$', PersonDetailView.as_view(), name='person_detail'),
    url(r'^vacancies/?$', VacanciesPageDetailView.as_view(), name='vacancies_page'),
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='people_page'),
]
