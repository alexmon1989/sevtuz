from django.contrib import admin
from apps.people.models import Page, Person, Position, PersonPhoto


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования страниц."""
    list_display = ('title', 'is_visible', 'created_at', 'updated_at')
    ordering = ('title',)
    list_editable = ('is_visible',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class PersonPhotoInline(admin.TabularInline):
    model = PersonPhoto
    extra = 3


class CurrentPlayInline(admin.TabularInline):
    model = Person.current_plays.through
    extra = 3


class LastPlayInline(admin.TabularInline):
    model = Person.last_plays.through
    extra = 3


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования сотрудников."""
    list_display = ('name', 'created_at', 'updated_at')
    ordering = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    inlines = (PersonPhotoInline, CurrentPlayInline, LastPlayInline)


@admin.register(Position)
class PositionsAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования должностей."""
    list_display = ('title', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    search_fields = ('title',)
