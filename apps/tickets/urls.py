from django.conf.urls import url
from apps.tickets.views import PageDetailView

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='tickets_page'),
]
