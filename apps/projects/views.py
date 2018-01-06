from django.views.generic import DetailView
from apps.projects.models import Page


class PageDetailView(DetailView):
    """Отображает страницу раздела Медиа."""
    model = Page
    template_name = "projects/page_detail/page_detail.html"
    queryset = Page.objects.filter(is_visible=True)
