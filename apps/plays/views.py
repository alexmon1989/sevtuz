from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.http import Http404

from apps.theater.models import Play


class PlayListView(ListView):
    """Отображает страницу со списком спектаклей театра."""
    model = Play
    template_name = 'plays/list/list.html'
    paginate_by = 10

    def get(self, *args, **kwargs):
        page = self.request.GET.get('page')
        if page:
            try:
                if int(page) == 1:
                    return redirect(self.request.resolver_match.url_name)
            except ValueError:
                raise Http404
        return super(PlayListView, self).get(*args, **kwargs)

    def get_queryset(self):
        qs = Play.objects.filter(is_our_play=True).order_by('created_at')

        full_path = self.request.get_full_path()

        statuses = ['current', 'archive', 'plans']
        for status in statuses:
            if status in full_path:
                qs = qs.filter(status=statuses.index(status)+1)

        return qs


class PlayDetailView(DetailView):
    """Отображает страницу со спектаклем."""
    model = Play
    template_name = 'plays/detail/detail.html'
