# simple_personal_site URL Configuration

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic.base import RedirectView
from blog.sitemaps import ArticleSitemap, TagSitemap
from home.views import handler404, handler500
from .sitemaps import SiteSitemap

sitemaps = {
    'site': SiteSitemap,
    'articles': ArticleSitemap,
    'tags': TagSitemap,
}

# url search order: favicon, sitemap, home, modules, admin, shortener
# media file is only served in DEBUG MODE1
urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.ico')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('projects/', include('projects.urls')),
    path('', include('url_shortener.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# get admin url from config
if settings.ADMIN_URL:
    urlpatterns.insert(3, path(settings.ADMIN_URL, admin.site.urls))
