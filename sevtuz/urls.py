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
from apps.theater import urls as theater_urls
from apps.contacts import urls as contacts_urls
from apps.tickets import urls as tickets_urls
from apps.people import urls as people_urls
from apps.playbill import urls as playbill_urls
from apps.media import urls as media_urls
from apps.projects import urls as projects_urls
from apps.search import urls as search_urls
from sevtuz.sitemap import (StaticSitemap, TheaterNewsSitemap, PlaysSitemap, PersonsSitemap, TheaterPagesSitemap,
                            PersonPagesSitemap, TheaterHistorySitemap, TicketsPagesSitemap, MediaPagesSitemap,
                            ProjectsPagesSitemap)
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'static': StaticSitemap,
    'plays': PlaysSitemap,
    'persons': PersonsSitemap,
    'theater_pages': TheaterPagesSitemap,
    'theater_news': TheaterNewsSitemap,
    'theater_history': TheaterHistorySitemap,
    'tickets_pages': TicketsPagesSitemap,
    'person_pages': PersonPagesSitemap,
    'media_pages': MediaPagesSitemap,
    'projects_pages': ProjectsPagesSitemap,
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^theater/', include(theater_urls)),
    url(r'^contacts/', include(contacts_urls)),
    url(r'^tickets/', include(tickets_urls)),
    url(r'^people/', include(people_urls)),
    url(r'^playbill/', include(playbill_urls)),
    url(r'^media-section/', include(media_urls)),
    url(r'^projects/', include(projects_urls)),
    url(r'^search', include(search_urls)),
    url(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps}),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
