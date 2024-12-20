from django import forms
from django.contrib import admin
from apps.theater.models import (Season, Play, PlayPhoto, PlayVideo, Genre, Page, Person, PersonPhoto, Position,
                                 PersonPlayRole, History, HistoryPhoto, HistoryVideo, Document, DocumentType,
                                 Partner, InternalEvent, PlayType)


class SeasonForm(forms.ModelForm):
    """Класс формы сезона."""
    def clean_year_to(self):
        """Валидация поля year_to."""
        year_from = self.cleaned_data['year_from']
        year_to = self.cleaned_data['year_to']
        if (year_to - year_from) != 1:
            raise forms.ValidationError('Значение поля должно быть больше на 1 чем значение поля "Год с"')
        return year_to

    def clean_month_to(self):
        """Валидация поля month_to."""
        month_from = self.cleaned_data['month_from']
        month_to = self.cleaned_data['month_to']
        if month_from <= month_to:
            raise forms.ValidationError('Значение поля должно быть больше чем значение поля "Месяц с"')
        return month_to

    class Meta:
        model = Season
        fields = ('title', 'year_from', 'year_to', 'month_from', 'month_to')


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования сезонов."""
    list_display = ('title', 'year_from', 'year_to', 'month_from', 'month_to', 'created_at', 'updated_at')
    ordering = ('year_from',)
    search_fields = ('title',)
    form = SeasonForm


class PlayPhotoInline(admin.TabularInline):
    model = PlayPhoto
    extra = 3


class PlayVideoInline(admin.TabularInline):
    model = PlayVideo
    extra = 3


class PlayRoleInline(admin.TabularInline):
    model = PersonPlayRole
    extra = 3


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования спектакля."""
    list_display = ('title', 'genre', 'status', 'age', 'created_at', 'updated_at')
    ordering = ('title',)
    search_fields = ('title',)
    list_filter = ('genre', 'status')
    inlines = (PlayPhotoInline, PlayVideoInline, PlayRoleInline)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования спектакля."""
    list_display = ('title', 'created_at', 'updated_at')
    ordering = ('title',)
    search_fields = ('title',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования страниц."""
    list_display = ('title', 'is_visible', 'weight', 'created_at', 'updated_at')
    ordering = ('title',)
    list_editable = ('is_visible', 'weight',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class PersonPhotoInline(admin.TabularInline):
    model = PersonPhoto
    extra = 3


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования сотрудников."""
    list_display = ('name', 'position', 'is_actor', 'has_page', 'created_at', 'updated_at')
    ordering = ('name',)
    exclude = ('user', )
    search_fields = ('name', 'position')
    list_filter = ('position', 'is_actor', 'has_page')
    prepopulated_fields = {"slug": ("name",)}
    inlines = (PersonPhotoInline,)


@admin.register(Position)
class PositionsAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования должностей."""
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)


class HistoryPhotoInline(admin.TabularInline):
    model = HistoryPhoto
    extra = 3


class HistoryVideoInline(admin.TabularInline):
    model = HistoryVideo
    extra = 3


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования новостей."""
    list_display = ('season', 'created_at', 'updated_at')
    ordering = ('season__year_from',)
    search_fields = ('season__title',)
    inlines = (HistoryPhotoInline, HistoryVideoInline)


@admin.register(Document)
class DocumentsAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования документов."""
    list_display = ('title', 'is_visible', 'created_at', 'updated_at')
    list_editable = ('is_visible',)
    search_fields = ('title',)


@admin.register(DocumentType)
class DocumentTypesAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования типов документов."""
    list_display = ('title', 'created_at', 'updated_at')
    ordering = ('title',)
    search_fields = ('title',)


@admin.register(Partner)
class PartnersAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования документов."""
    list_display = ('title', 'link', 'is_visible', 'created_at', 'updated_at')
    list_editable = ('is_visible',)
    search_fields = ('title', 'link')


@admin.register(InternalEvent)
class InternalEventsAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования внутренних событий."""
    list_display = ('title', 'start', 'end', 'responsible_person', 'is_visible', 'created_at', 'updated_at')
    list_editable = ('is_visible',)
    search_fields = ('title',)


@admin.register(PlayType)
class PlayTypeAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования типов спектклей."""
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
