from django.views.generic import DetailView
from apps.media.models import Page


class PageDetailView(DetailView):
    """Отображает страницу раздела Медиа."""
    model = Page
    template_name = "media/page_detail/page_detail.html"
    queryset = Page.objects.filter(is_visible=True)
