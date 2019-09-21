from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from global_config.site_config import SITE_PROTOCOL


class SiteSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'
    protocol = SITE_PROTOCOL

    def items(self):
        return ['homepage', 'blog', 'projects']

    def location(self, obj):
        return reverse(obj)
