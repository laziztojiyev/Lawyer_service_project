from django.contrib import admin
from django.urls import path

from apps.views import IndexView, AboutView, GetFormView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', GetFormView.as_view(), name='contact')
]
