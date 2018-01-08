from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views.generic import ListView
from django.shortcuts import render
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404

from apps.theater.models import News, History, Play, Person, Page as TheaterPage, Document
from apps.tickets.models import Page as TicketsPage
from apps.people.models import Page as PeoplePage
from apps.media.models import Page as MediaPage
from apps.projects.models import Page as ProjectsPage
from apps.contacts.models import Page as ContactsPage


def search(request):
    """Отображает страницу результатов поиска."""
    keywords = request.GET.get('q')
    if not keywords:
        raise Http404("Поисковый запрос пустой.")

    results = []

    # Источники поиска (модели)
    sources = [
        {'model': News, 'title_field': 'title', 'text_field': 'text'},
        {'model': Play, 'title_field': 'title', 'text_field': 'text'},
        {'model': Person, 'title_field': 'name', 'text_field': 'biography'},
        {'model': History, 'title_field': 'season__title', 'text_field': 'text'},
        {'model': TheaterPage, 'title_field': 'title', 'text_field': 'text'},
        {'model': TicketsPage, 'title_field': 'title', 'text_field': 'text'},
        {'model': PeoplePage, 'title_field': 'title', 'text_field': 'text'},
        {'model': MediaPage, 'title_field': 'title', 'text_field': 'text'},
        {'model': ProjectsPage, 'title_field': 'title', 'text_field': 'text'},
        {'model': Document, 'title_field': 'title', 'text_field': None},
        {'model': ContactsPage, 'title_field': None, 'text_field': 'text'},
    ]

    # В зависимости от фильтра убираются источники
    if request.GET.get('source'):
        if 'others' not in request.GET.getlist('source'):
            sources = sources[0:3]
        if 'theater_news' not in request.GET.getlist('source'):
            sources.remove({'model': News, 'title_field': 'title', 'text_field': 'text'})
        if 'theater_play' not in request.GET.getlist('source'):
            sources.remove({'model': Play, 'title_field': 'title', 'text_field': 'text'})
        if 'theater_person' not in request.GET.getlist('source'):
            sources.remove({'model': Person, 'title_field': 'name', 'text_field': 'biography'})

    # Для каждого источника поиска производится полнотекстовый поиск
    for source in sources:
        try:
            source['model']._meta.get_field('is_visible')
            qs = source['model'].objects.filter(is_visible=True)
        except models.FieldDoesNotExist:
            qs = source['model'].objects.all()

        query = SearchQuery(keywords, config='russian')

        vectors = None
        if source.get('title_field'):
            title_vector = SearchVector(source['title_field'], weight='A', config='russian')
            vectors = title_vector
        if source.get('text_field'):
            content_vector = SearchVector(source['text_field'], weight='B', config='russian')
            try:
                vectors += content_vector
            except TypeError:
                vectors = content_vector

        qs = qs.annotate(search=vectors).filter(search=query)
        qs = qs.annotate(rank=SearchRank(vectors, query))
        if source.get('text_field'):
            qs = qs.extra(
                select={
                    'headline_text': f"ts_headline(\"{source['model']._meta.db_table}\".\"{source['text_field']}\", plainto_tsquery( %s ), 'StartSel=<em>, StopSel=</em>')",
                    'source_type': "%s"
                },
                select_params=(keywords, source['model']._meta.db_table)
            )
        if len(qs) > 0:
            for item in qs:
                results.append(item)

    # Сортировка результатов поиска по rank
    results = sorted(results, key=lambda x: x.rank, reverse=True)
    count_results = len(results)

    # Пагинация
    paginator = Paginator(results, 10)  # Показывать 10 результатов поиска на странице
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        # Если параметр page не integer, показать первую страницу
        results = paginator.page(1)
    except EmptyPage:
        # Если параметр page вне диапазона (напр., 9999), показать последнюю страницу.
        results = paginator.page(paginator.num_pages)

    return render(request, 'search/search.html',
                  {'results': results, 'count': count_results, 'sources_selected': request.GET.getlist('source')})
