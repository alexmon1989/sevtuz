from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from apps.pushkin_card.models import Page

admin.site.register(Page, SingleModelAdmin)
