from django.db import models
from media.models import Embed, Image


class ProjectsConfig(models.Model):
    projects_per_page = models.IntegerField(blank=False, default=6)

    class Meta:
        verbose_name = '# Projects Config #'


class Project(models.Model):
    title = models.CharField(verbose_name='Project Name', max_length=100, default='', null=False, unique=True)
    description = models.TextField(verbose_name='Project Description', default='', null=False,
                                   help_text="Write in Markdown format")
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.CASCADE,
                              help_text="If both are selected, only embedded media will show on screen.")
    embed = models.ForeignKey(Embed, blank=True, null=True, on_delete=models.CASCADE,
                              help_text="<strong>When printing, only image will show.</strong><br>"
                                        "If both are selected, only embedded media will show on screen.")
    url = models.URLField(verbose_name='Project URL', null=False, blank=True)
    posted = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-posted', 'title']

    def __str__(self):
        return self.title
