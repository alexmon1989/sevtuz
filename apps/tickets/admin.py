from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from apps.tickets.models import Page

admin.site.register(Page, SingleModelAdmin)
