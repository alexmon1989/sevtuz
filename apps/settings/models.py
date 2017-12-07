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


class SocialLinksModel(models.Model):
    """Настройки ссылок на соц. сети."""
    fb = models.URLField('Facebook', max_length=255, null=True, blank=True)
    vk = models.URLField('Вконтакте', max_length=255, null=True, blank=True)
    instagram = models.URLField('Instagram', max_length=255, null=True, blank=True)
    ok = models.URLField('Одноклассники', max_length=255, null=True, blank=True)
    twitter = models.URLField('Twitter', max_length=255, null=True, blank=True)
    youtube = models.URLField('Youtube', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Ссылки на соц. сети'
        verbose_name_plural = 'Ссылки на соц. сети'


class Analytics(models.Model):
    """Модель HTML-кода аналитики."""
    code = models.TextField('HTML-код')
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'HTML-код аналитики'
        verbose_name_plural = 'HTML-код аналитики'
