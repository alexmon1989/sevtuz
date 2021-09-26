from django.views.generic import DetailView
from django.shortcuts import render
from apps.theater.models import Person
from apps.people.models import Page


def pages_list(request):
    """Отображает страницу со списком сраниц приложения."""
    page_list = Page.objects.filter(is_visible=True)
    return render(request, 'people/page_list.html', {'page_list': page_list})


class PageDetailView(DetailView):
    """Отображает страницу раздела Люди театра."""
    model = Page
    template_name = "people/page_detail/page_detail.html"
    queryset = Page.objects.filter(is_visible=True)


class PersonDetailView(DetailView):
    """Отображает страницу сотрудника."""
    model = Person
    template_name = "people/person_detail/person_detail.html"
    queryset = Person.objects.filter(has_page=True)
