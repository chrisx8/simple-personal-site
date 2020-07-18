# url_shortener URL Configuration

from django.urls import path
from . import views

urlpatterns = [
    path('<str:alias>/', views.redirect),
]
