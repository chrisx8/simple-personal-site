from django.db import models


class Project(models.Model):
    title = models.CharField(verbose_name='Project Name', max_length=100, default='', null=False)
    description = models.TextField(verbose_name='Project Description', default='', null=False)
    image = models.FileField(verbose_name='Project Image', upload_to='projects', blank=True)
    youtube_id = models.CharField(verbose_name='Youtube Video ID', max_length=15, blank=True)
    url = models.URLField(verbose_name='Project URL', null=False, default='')
    url_description = models.CharField(verbose_name='URL Description', max_length=50, default='Website', null=False)
    fa_icon = models.CharField(verbose_name='Font Awesome icon class', max_length=50, default='', 
                               null=False, blank=True)

    def __str__(self):
        return self.title
