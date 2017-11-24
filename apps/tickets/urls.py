from django.conf.urls import url
from apps.tickets.views import page_detail

urlpatterns = [
    url(r'^$', page_detail, name='tickets'),
]
