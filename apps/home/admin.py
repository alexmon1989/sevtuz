from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from apps.home.models import Playbill

admin.site.register(Playbill, SingleModelAdmin)
