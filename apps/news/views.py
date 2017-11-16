from django.views.generic import ListView, DetailView
from apps.news.models import News
from apps.theater.models import Season


class NewsListView(ListView):
    """Отображает страницу со списком новостей."""
    model = News
    template_name = 'news/list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = News.objects.filter(is_visible=True).order_by('-created_at')

        if self.request.GET.get('year') and self.request.GET.get('month'):
            """Если определены параметры года и месяца, то применяется фильтр по ним."""
            try:
                qs = qs.filter(
                    created_at__year=int(self.request.GET.get('year')),
                    created_at__month=int(self.request.GET.get('month'))
                )
            except ValueError:
                pass
        return qs

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['seasons'] = Season.objects.order_by('-created_at')[:3]
        context['months'] = Season.MONTHS_CHOICES
        if self.request.GET.get('year') and self.request.GET.get('month'):
            try:
                context['month_title'] = Season.MONTHS_CHOICES[int(self.request.GET.get('month')) - 1][1]
            except ValueError:
                pass
        return context


class NewsDetailView(DetailView):
    """Отображает страницу с новостью."""
    model = News
    template_name = 'news/detail.html'
    queryset = News.objects.filter(is_visible=True)

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['more_news'] = self.queryset.filter(is_visible=True).order_by('-created_at').exclude(
            pk=self.kwargs['pk']
        )[:3]
        context['seasons'] = Season.objects.order_by('-created_at')[:3]
        return context
