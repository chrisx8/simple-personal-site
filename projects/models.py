from django.db import models
from media.models import Image, Video


class Project(models.Model):
    title = models.CharField(verbose_name='Project Name', max_length=100, default='', null=False)
    description = models.TextField(verbose_name='Project Description', default='', null=False,
                                   help_text="Write in Markdown format")
    image = models.ForeignKey(Image, verbose_name='Project Image', on_delete=models.CASCADE, null=True, blank=True,
                              help_text="When both image and video are selected, only video will show.")
    video = models.ForeignKey(Video, verbose_name='Project Video', on_delete=models.CASCADE, null=True, blank=True,
                              help_text="When both image and video are selected, only video will show.")
    url = models.URLField(verbose_name='Project URL', null=False, blank=True)
    url_description = models.CharField(verbose_name='URL Description', max_length=50, default='Website', blank=True)
    fa_icon = models.CharField(verbose_name='Font Awesome icon class', max_length=50, default='',
                               null=False, blank=True)
    show = models.BooleanField(verbose_name='Show on Projects page', default=True, null=False)

    def __str__(self):
        return self.title
