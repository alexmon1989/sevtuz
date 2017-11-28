from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from apps.news.models import News
from apps.theater.models import Play, Page as TheaterPage, Person
from apps.people.models import Page as PersonPage


class StaticSitemap(Sitemap):
    def items(self):
        return [
            'home',
            'contacts',
            'tickets',
            'events_list',
            'plays_list_current',
            'plays_list_archive',
            'plays_list_plans',
        ]

    def location(self, item):
        return reverse(item)


class NewsSitemap(Sitemap):
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
