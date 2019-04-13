from django.db import models


class Homepage(models.Model):
    about_me = models.TextField(verbose_name='About Me section', default='', null=False,
                                help_text='Write in Markdown format')
    resume = models.FileField(blank=True, help_text='Upload resume as a PDF for best compatibility')
