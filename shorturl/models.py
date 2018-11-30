from django.db import models


class ShortURL(models.Model):
    alias = models.CharField(primary_key=True, max_length=50, default='', null=False,
                             help_text='Example: XYZ is the alias in shortened URL example.com/go/XYZ')
    full_url = models.URLField(default='', null=False)
    enabled = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.alias
