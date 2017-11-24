from django.views.generic import DetailView
from apps.theater.models import Page


class PageDetailView(DetailView):
    """Отображает страницу с новостью."""
    model = Page
    queryset = Page.objects.filter(is_visible=True)
