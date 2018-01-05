from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from apps.people.models import Page, Vacancy, VacanciesPage


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования страниц."""
    list_display = ('title', 'is_visible', 'created_at', 'updated_at')
    ordering = ('title',)
    list_editable = ('is_visible',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Vacancy)
class VacationAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования страниц."""
    list_display = ('title', 'count', 'created_at', 'updated_at')
    ordering = ('title',)
    search_fields = ('title',)


"""Интерфейс администрирования страниц."""
admin.site.register(VacanciesPage, SingleModelAdmin)
