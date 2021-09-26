from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, get_object_or_404
from django.http import Http404
from apps.theater.models import Page, History, DocumentType


class PageDetailView(DetailView):
    """Отображает статичную страницу приложения."""
    model = Page
    template_name = 'theater/pages/page_detail.html'
    queryset = Page.objects.filter(is_visible=True)


class HistoryDetailView(DetailView):
    """Отображает страницу с историей сезона."""
    model = History
    template_name = 'theater/history/detail.html'

    def get(self, *args, **kwargs):
        if not self.kwargs.get('pk'):
            try:
                history = History.objects.order_by('-season__year_from').first()
                return redirect('theater_history', pk=history.pk)
            except AttributeError:
                raise Http404
        self.object = self.get_object()
        return super(HistoryDetailView, self).get(*args, **kwargs)

    def get_object(self):
        return get_object_or_404(History, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super(HistoryDetailView, self).get_context_data(**kwargs)
        context['media_count'] = len(self.object.get_videos()) + len(self.object.get_photos())
        context['histories'] = History.objects.order_by('-season__year_from')
        return context


class DocumentTypeListView(ListView):
    """Отображает страницу с типами документов."""
    model = DocumentType
    template_name = 'theater/document_types/list.html'
