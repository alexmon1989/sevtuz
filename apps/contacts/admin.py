from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from apps.contacts.models import Page

admin.site.register(Page, SingleModelAdmin)
