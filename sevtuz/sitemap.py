from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from apps.theater.models import News, Play, Page as TheaterPage, Person, History
from apps.tickets.models import Page as TicketPage
from apps.people.models import Page as PersonPage


class StaticSitemap(Sitemap):
    def items(self):
        return [
            'home',
            'contacts',
            'events_list',
            'plays_list_current',
            'plays_list_archive',
            'plays_list_plans',
        ]

    def location(self, item):
        return reverse(item)


class TheaterNewsSitemap(Sitemap):
    def items(self):
        return History.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class TheaterHistorySitemap(Sitemap):
    def items(self):
        return News.objects.filter(is_visible=True)

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
