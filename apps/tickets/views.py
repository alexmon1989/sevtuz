from django.views.generic import DetailView
from apps.tickets.models import Page


class PageDetailView(DetailView):
    """Отображает страницу приложения."""
    model = Page
    queryset = Page.objects.filter(is_visible=True)
