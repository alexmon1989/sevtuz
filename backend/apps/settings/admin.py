from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from apps.settings.models import FooterSettings, SocialLinksModel, Analytics, HeaderSettings

admin.site.register(FooterSettings, SingleModelAdmin)
admin.site.register(HeaderSettings, SingleModelAdmin)
admin.site.register(SocialLinksModel, SingleModelAdmin)
admin.site.register(Analytics, SingleModelAdmin)
