from djangoseo import seo


class MyMetadata(seo.Metadata):
    title = seo.Tag(head=True, max_length=68)
    description = seo.MetaTag(max_length=155)
    keywords = seo.KeywordTag()
    heading = seo.Tag(name="h1")

    class HelpText:
        title = "Это будет отображаться в названии окна / вкладки, а также в результатах поиска."
        description = "Краткое описание содержимого страницы. Это будет отображаться в результатах поиска."
        keywords = "Список слов или фраз, разделенных запятыми, которые описывают контент."
        heading = "Это будет отображаться в элементе h1."

    class Meta:
        seo_models = (
            'news.News',
            'contacts.Page',
            'people.Page',
            'tickets.Page',
            'theater.Page',
            'theater.Person',
            'theater.Play',
        )
        verbose_name = "SEO"
        verbose_name_plural = "SEO"
        backends = ('path', 'modelinstance')
