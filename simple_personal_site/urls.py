# simple_personal_site URL Configuration

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from home.views import handler403, handler404, handler500

# url search order: favicon, sitemap, home, modules, admin, shortener
# media file is only served in DEBUG MODE
urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.ico')),
    path('contact/', include('contact.urls')),
]

# enable admin if url is configured
if settings.ADMIN_URL:
    urlpatterns.append(path(settings.ADMIN_URL, admin.site.urls))
