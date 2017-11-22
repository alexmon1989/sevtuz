from django.db import models


class FooterSettings(models.Model):
    """Настройки футера."""
    information_block_title = models.CharField('Заголовок текстового блока', max_length=100, null=True, blank=True)
    information_block_text = models.TextField('Текст блока (html)', null=True, blank=True)
    contacts_block_html = models.TextField(
        'Текст блока "Контакты" (html)',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'
