# contact URL Configuration

from django.urls import path

from . import views

urlpatterns = [
    path("", views.contact, name="contact"),
    path("pgp_key.asc", views.pgp_key, name="pgp_key"),
]
