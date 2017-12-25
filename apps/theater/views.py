from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, reverse
from django.http import Http404
from apps.theater.models import Page, News, Season


class PageDetailView(DetailView):
    """Отображает статичную страницу приложения."""
    model = Page
    queryset = Page.objects.filter(is_visible=True)


class NewsListView(ListView):
    """Отображает страницу со списком новостей."""
    model = News
    template_name = 'theater/news/list.html'
    paginate_by = 5

    def get(self, *args, **kwargs):
        page = self.request.GET.get('page')
        if page:
            try:
                if int(page) == 1:
                    if len(self.request.GET) == 1:
                        return redirect(self.request.resolver_match.url_name)
                    else:
                        dict_ = self.request.GET.copy()
                        dict_.pop('page')
                        return redirect('{}?{}'.format(reverse('theater_news_list'), dict_.urlencode()))
            except ValueError:
                raise Http404
        return super(NewsListView, self).get(*args, **kwargs)

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
        context['seasons'] = Season.objects.order_by('-year_to')[:3]
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
    template_name = 'theater/news/detail.html'
    queryset = News.objects.filter(is_visible=True)

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['more_news'] = self.queryset.filter(is_visible=True).order_by('-created_at').exclude(
            slug=self.kwargs['slug']
        )[:3]
        context['seasons'] = Season.objects.order_by('-created_at')[:3]
        return context
