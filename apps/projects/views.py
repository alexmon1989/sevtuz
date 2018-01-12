from django.views.generic import DetailView, ListView
from apps.projects.models import Page


class PageDetailView(DetailView):
    """Отображает страницу раздела Медиа."""
    model = Page
    queryset = Page.objects.filter(is_visible=True)


class PageListView(ListView):
    """Отображает страницу со списком сраниц."""
    model = Page
    queryset = Page.objects.filter(is_visible=True)
