from django.contrib import admin
from apps.projects.models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования страниц."""
    list_display = ('title', 'is_visible', 'weight', 'created_at', 'updated_at')
    ordering = ('title',)
    list_editable = ('is_visible', 'weight',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('is_visible',)


# django-seo
from django.contrib.sites.models import Site
from djangoseo.admin import register_seo_admin, auto_register_inlines
from sevtuz.seo import MyMetadata

# django-seo
register_seo_admin(admin.site, MyMetadata)
auto_register_inlines(admin.site, MyMetadata)
admin.site.unregister(Site)
