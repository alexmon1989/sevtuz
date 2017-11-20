from django.views.generic import ListView
from apps.playbill.models import Event
from datetime import datetime


class EventListView(ListView):
    """Отображает страницу со списком событий."""
    model = Event
    template_name = 'playbill/events/list.html'
    paginate_by = 5

    def get_queryset(self):
        month = datetime.now().month
        qs = Event.objects.filter(is_visible=True, datetime__month=month).order_by('datetime')
        return qs

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        return context
