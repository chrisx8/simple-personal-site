from django.db import models
from media.models import Embed, Image


class Project(models.Model):
    title = models.CharField(verbose_name='Project Name', max_length=100, default='', null=False, unique=True)
    description = models.TextField(verbose_name='Project Description', default='', null=False,
                                   help_text="Write in Markdown format")
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.CASCADE,
                              help_text="If both are selected, only embedded media will show on screen.")
    embed = models.ForeignKey(Embed, blank=True, null=True, on_delete=models.CASCADE,
                              help_text="If both are selected, only embedded media will show on screen.<br>"
                                        "<strong>When printing, only image will show.</strong>")
    url = models.URLField(verbose_name='Project URL', null=False, blank=True)
    order = models.IntegerField(verbose_name="Sort order", unique=True, null=False,
                                help_text="Projects are ordered by this number (from smallest to largest).<br>"
                                "<strong>No duplicates allowed.</strong>")

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
