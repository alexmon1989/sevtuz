from django.contrib import admin
from apps.media.models import Page, News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования новостей."""
    list_display = ('title', 'is_visible', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    list_editable = ('is_visible',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования страниц."""
    list_display = ('title', 'is_visible', 'weight', 'created_at', 'updated_at')
    ordering = ('title',)
    list_editable = ('is_visible', 'weight',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('is_visible',)
