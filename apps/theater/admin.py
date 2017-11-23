from django import forms
from django.contrib import admin
from apps.theater.models import Season, Play, PlayPhoto, PlayVideo, Genre, Page


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
    ordering = ('-created_at',)
    search_fields = ('title',)
    form = SeasonForm


class PlayPhotoInline(admin.TabularInline):
    model = PlayPhoto
    extra = 3


class PlayVideoInline(admin.TabularInline):
    model = PlayVideo
    extra = 3


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования спектакля."""
    list_display = ('title', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    search_fields = ('title',)
    inlines = (PlayPhotoInline, PlayVideoInline)
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
    list_display = ('title', 'is_visible', 'created_at', 'updated_at')
    ordering = ('title',)
    list_editable = ('is_visible',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
