from django.views.generic import DetailView
from apps.people.models import Page, Person


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
