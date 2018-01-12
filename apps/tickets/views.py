from django.views.generic import DetailView, ListView
from apps.tickets.models import Page


class PageDetailView(DetailView):
    """Отображает страницу приложения."""
    model = Page
    queryset = Page.objects.filter(is_visible=True)


class PageListView(ListView):
    """Отображает страницу со списком сраниц."""
    model = Page
    queryset = Page.objects.filter(is_visible=True)
