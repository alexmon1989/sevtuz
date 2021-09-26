from django.conf.urls import url
from apps.contacts.views import page_detail

urlpatterns = [
    url(r'^$', page_detail, name='contacts'),
]
