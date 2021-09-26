from django.conf.urls import url
from apps.search.views import search

urlpatterns = [
    url(r'^$', search, name='search'),
]
