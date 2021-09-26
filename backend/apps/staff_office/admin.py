from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import Office

admin.site.register(Office, SingleModelAdmin)
