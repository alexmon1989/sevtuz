from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.theater.models import News, Play, Page as TheaterPage, Person, History
from apps.tickets.models import Page as TicketPage
from apps.people.models import Page as PersonPage
from apps.media.models import Page as MediaPage
from apps.projects.models import Page as ProjectsPage


class StaticSitemap(Sitemap):
    def items(self):
        return [
            'home',
            'contacts',
            'playbill_events_list',
            'playbill_plays_current',
            'playbill_plays_archive',
            'playbill_plays_plans',
            'vacancies_page',
        ]

    def location(self, item):
        return reverse(item)


class TheaterNewsSitemap(Sitemap):
    def items(self):
        return News.objects.filter(is_visible=True)

    def lastmod(self, obj):
        return obj.updated_at


class TheaterHistorySitemap(Sitemap):
    def items(self):
        return History.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class PlaysSitemap(Sitemap):
    def items(self):
        return Play.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class TheaterPagesSitemap(Sitemap):
    def items(self):
        return TheaterPage.objects.filter(is_visible=True)

    def lastmod(self, obj):
        return obj.updated_at


class TicketsPagesSitemap(Sitemap):
    def items(self):
        return TicketPage.objects.filter(is_visible=True)

    def lastmod(self, obj):
        return obj.updated_at


class PersonPagesSitemap(Sitemap):
    def items(self):
        return PersonPage.objects.filter(is_visible=True)

    def lastmod(self, obj):
        return obj.updated_at


class PersonsSitemap(Sitemap):
    def items(self):
        return Person.objects.filter(has_page=True)

    def lastmod(self, obj):
        return obj.updated_at


class MediaPagesSitemap(Sitemap):
    def items(self):
        return MediaPage.objects.filter(is_visible=True)

    def lastmod(self, obj):
        return obj.updated_at


class ProjectsPagesSitemap(Sitemap):
    def items(self):
        return ProjectsPage.objects.filter(is_visible=True)

    def lastmod(self, obj):
        return obj.updated_at
