from django.contrib import admin
from apps.playbill.models import Event, Scene


@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования сцены."""
    list_display = ('title', 'show_in_filter', 'created_at', 'updated_at')
    ordering = ('title',)
    search_fields = ('title',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования события."""
    list_display = ('play', 'datetime', 'is_visible', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    search_fields = ('title',)


# django-seo
from django.contrib.sites.models import Site
from djangoseo.admin import register_seo_admin, auto_register_inlines
from apps.home.seo import MyMetadata

# django-seo
register_seo_admin(admin.site, MyMetadata)
auto_register_inlines(admin.site, MyMetadata)
admin.site.unregister(Site)
