from django.db import models


class URL(models.Model):
    alias = models.CharField(primary_key=True, max_length=50, default='', null=False,
                             help_text='Example: XYZ is the alias in shortened URL example.com/XYZ<br>' +
                                       '<strong>Alias can\'t be one of the built-in paths (blog, contact, ' +
                                       'projects, media, static, favicon.ico, sitemap.xml)')
    full_url = models.URLField(default='', null=False)

    class Meta:
        ordering = ['alias']
        verbose_name = 'URL'

    def __str__(self):
        return self.alias
