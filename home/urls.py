# home URL Configuration

from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("skipsetup/", views.skip_setup, name="skip_setup"),
]
