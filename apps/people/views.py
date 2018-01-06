from django.views.generic import DetailView
from apps.theater.models import Person
from apps.people.models import Page, VacanciesPage


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


class VacanciesPageDetailView(DetailView):
    """Отображает страницу Вакансии."""
    model = VacanciesPage
    template_name = "people/vacancies_page/page_detail.html"

    def get_object(self):
        page, created = VacanciesPage.objects.get_or_create()
        return page
