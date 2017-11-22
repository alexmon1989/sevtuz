from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from apps.home.models import MainEvent

admin.site.register(MainEvent, SingleModelAdmin)
