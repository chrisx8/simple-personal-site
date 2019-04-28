from django.contrib.sitemaps import Sitemap
from .models import Article, Tag
from global_config.site_config import SITE_PROTOCOL


class ArticleSitemap(Sitemap):
    priority = 0.8
    protocol = SITE_PROTOCOL

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.last_edited


class TagSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'
    protocol = SITE_PROTOCOL

    def items(self):
        return Tag.objects.all()
