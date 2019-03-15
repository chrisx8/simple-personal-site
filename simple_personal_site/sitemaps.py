from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class HomepageSitemap(Sitemap):
    priority = 1.0

    def items(self):
        return ['homepage']

    def location(self, obj):
        return reverse(obj)


class SiteSitemap(Sitemap):
    priority = 0.9

    def items(self):
        return ['blog', 'projects', 'contact']

    def location(self, obj):
        return reverse(obj)
