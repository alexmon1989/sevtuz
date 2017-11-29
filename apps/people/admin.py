from django.contrib import admin
from apps.people.models import Page

# django-seo
from django.contrib.sites.models import Site
from djangoseo.admin import register_seo_admin, auto_register_inlines
from apps.home.seo import MyMetadata


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования страниц."""
    list_display = ('title', 'is_visible', 'created_at', 'updated_at')
    ordering = ('title',)
    list_editable = ('is_visible',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


# django-seo
register_seo_admin(admin.site, MyMetadata)
auto_register_inlines(admin.site, MyMetadata)
admin.site.unregister(Site)
