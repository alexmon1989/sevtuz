from django.views.generic import DetailView
from apps.theater.models import Play


class PlayDetailView(DetailView):
    """Отображает страницу со спектаклем."""
    model = Play
    template_name = 'theater/play/detail.html'
