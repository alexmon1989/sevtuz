from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from apps.settings.models import FooterSettings, SocialLinksModel

admin.site.register(FooterSettings, SingleModelAdmin)
admin.site.register(SocialLinksModel, SingleModelAdmin)
