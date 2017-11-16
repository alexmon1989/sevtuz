from django.db import models


class Season(models.Model):
    MONTHS_CHOICES = (
        (1, 'Январь'),
        (2, 'Февраль'),
        (3, 'Март'),
        (4, 'Апрель'),
        (5, 'Май'),
        (6, 'Июнь'),
        (7, 'Июль'),
        (8, 'Август'),
        (9, 'Сентябрь'),
        (10, 'Октябрь'),
        (11, 'Ноябрь'),
        (12, 'Декабрь'),
    )

    title = models.CharField('Название', max_length=255)
    year_from = models.PositiveIntegerField('Год с', default=None)
    year_to = models.PositiveIntegerField('Год по', default=None)
    month_from = models.PositiveIntegerField('Месяц с', choices=MONTHS_CHOICES, default=None)
    month_to = models.PositiveIntegerField('Месяц по', choices=MONTHS_CHOICES, default=None)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'
