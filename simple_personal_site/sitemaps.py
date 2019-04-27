from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from simple_personal_site.site_config import SITE_PROTOCOL


class SiteSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'
    protocol = SITE_PROTOCOL

    def items(self):
        return ['global_config', 'blog', 'projects', 'contact']

    def location(self, obj):
        return reverse(obj)
