from django.contrib.sitemaps import Sitemap
from .models import Article


class ArticleSitemap(Sitemap):
    priority = 0.8

    def items(self):
        return Article.objects.filter(show=True)

    def lastmod(self, obj):
        return obj.last_edited
