from django.db import models

from projects.models import Project


class Homepage(models.Model):
    about_me = models.TextField(verbose_name='About Me section', default='', null=False,
                                help_text='Write in Markdown format')
    featured_projects = models.ManyToManyField(Project, blank=True)
