from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from simple_personal_site.site_config import SITE_PROTOCOL


class SiteSitemap(Sitemap):
    priority = 1.0
    protocol = SITE_PROTOCOL

    def items(self):
        return ['homepage', 'blog', 'projects', 'contact']

    def location(self, obj):
        return reverse(obj)
