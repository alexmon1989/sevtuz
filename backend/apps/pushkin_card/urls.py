from django.urls import path
from apps.pushkin_card.views import index

urlpatterns = [
    path('', index, name='pushkin_card'),
]
