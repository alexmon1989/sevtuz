"""sevtuz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from apps.home.views import home
from apps.news import urls as news_urls
from apps.repertoire import urls as repertoire_urls
from apps.theater import urls as theater_urls
from apps.plays import urls as plays_urls
from apps.contacts import urls as contacts_urls
from apps.tickets import urls as tickets_urls
from apps.people import urls as people_urls
from sevtuz.sitemap import (StaticSitemap, NewsSitemap, PlaysSitemap, PersonsSitemap, TheaterPagesSitemap,
                            PersonPagesSitemap)
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'static': StaticSitemap,
    'news': NewsSitemap,
    'plays': PlaysSitemap,
    'persons': PersonsSitemap,
    'theater_pages': TheaterPagesSitemap,
    'person_pages': PersonPagesSitemap,
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^news/', include(news_urls)),
    url(r'^repertoire/', include(repertoire_urls)),
    url(r'^theater/', include(theater_urls)),
    url(r'^plays/', include(plays_urls)),
    url(r'^contacts/', include(contacts_urls)),
    url(r'^tickets/', include(tickets_urls)),
    url(r'^people/', include(people_urls)),
    url(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps}),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
