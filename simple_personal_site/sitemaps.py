from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class SiteSitemap(Sitemap):
    priority = 1.0

    def items(self):
        return ['homepage', 'blog', 'projects', 'contact']

    def location(self, obj):
        return reverse(obj)
