from django.contrib.sitemaps import Sitemap

from .models import Article, Tag


class ArticleSitemap(Sitemap):
    priority = 1.0
    changefreq = "daily"

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.last_edited


class TagSitemap(Sitemap):
    priority = 0.8
    changefreq = "daily"

    def items(self):
        return Tag.objects.all()
