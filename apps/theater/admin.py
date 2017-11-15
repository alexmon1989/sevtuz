from django.contrib import admin
from apps.theater.models import Season


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования сезонов."""
    list_display = ('title', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    search_fields = ('title',)
