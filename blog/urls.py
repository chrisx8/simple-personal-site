# Blog URL Configuration

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<str:article_id>/', views.view_article, name='view_article'),
    path('tag/<str:tag>/', views.blog, name='filter_by_tag'),
]
