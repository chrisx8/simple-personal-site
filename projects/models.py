from django.db import models
from media.models import Embed, Image


class ProjectsConfig(models.Model):
    description = models.CharField(max_length=250, default='', blank=True,
                                   help_text='This field sets the Meta Description tag for /projects/. Leave blank to '
                                             'use global Meta Description tag.')
    projects_per_page = models.IntegerField(blank=False, default=6)

    class Meta:
        verbose_name = '# Projects Config #'


class Project(models.Model):
    title = models.CharField(verbose_name='Project Name', max_length=100, default='', null=False, unique=True)
    description = models.TextField(verbose_name='Project Description', default='', null=False,
                                   help_text="Write in Markdown format")
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True,
                              help_text="When both are selected, only embedded media will show.")
    embed = models.ForeignKey(Embed, on_delete=models.CASCADE, null=True, blank=True,
                              help_text="When both are selected, only embedded media will show.")
    url = models.URLField(verbose_name='Project URL', null=False, blank=True)
    posted = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-posted', 'title']

    def __str__(self):
        return self.title
