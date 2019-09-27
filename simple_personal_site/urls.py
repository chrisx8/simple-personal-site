"""simple_personal_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.shortcuts import render
from django.urls import include, path
from django.views.generic.base import RedirectView
from blog.sitemaps import ArticleSitemap, TagSitemap
from .settings import ADMIN_URL, STATIC_URL
from .sitemaps import SiteSitemap

sitemaps = {
    'site': SiteSitemap,
    'articles': ArticleSitemap,
    'tags': TagSitemap,
}

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=STATIC_URL + 'icons/favicon.ico')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', include('homepage.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('go/', include('shorturl.urls')),
    path('projects/', include('projects.urls')),
]

# get admin url from config
if ADMIN_URL:
    urlpatterns.append(path(ADMIN_URL, admin.site.urls))


# 404 error page
def handler404(request, *args, **argv):
    return render(request, '404.html', status=404)


# 500 error page
def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)
