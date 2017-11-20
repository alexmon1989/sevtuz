from django.contrib import admin
from apps.playbill.models import Event, Scene


@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования сцены."""
    list_display = ('title', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    search_fields = ('title',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования события."""
    list_display = ('play', 'datetime', 'is_visible', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    search_fields = ('title',)
