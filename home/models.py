import os
from django.contrib import admin
from django.db import models
from django.dispatch import receiver
from solo.models import SingletonModel


class SiteInfo(SingletonModel):
    site_name = models.CharField(max_length=50, default='My Site', blank=False)
    site_url = models.URLField(default='http://example.com', blank=False, verbose_name='Site URL',
                               help_text='Include "http://" or "https://". No trailing slashes.')
    # meta description
    description = models.CharField(max_length=250, default='', blank=True,
                                   help_text='This field sets the global Meta Description tag.')
    # site header on every page
    header_title = models.CharField(max_length=250, default='My Site', blank=False)
    header_subtitle = models.CharField(max_length=250, blank=True)
    # copyright footer on every page
    footer_copyright = models.CharField(max_length=250, default='Simple Personal Site by chrisx8.',
                                        help_text='"&copy; YEAR " always shows. Set this to be the text after '
                                                  '"&copy; YEAR "')

    class Meta:
        verbose_name = '# Site Info #'
    
    def save(self, *args, **kwargs):
        admin.site.site_title = self.site_name
        admin.site.site_header = self.site_name
        super(SiteInfo, self).save(*args, **kwargs)


class SocialMediaLink(models.Model):
    platform = models.CharField(max_length=50, default='', null=False, help_text='Name of the social media platform')
    url = models.URLField(default='', null=False, verbose_name='URL', help_text='Link to profile page')

    class Meta:
        ordering = ['platform']
        verbose_name = 'Social Media Link'

    def __str__(self):
        return self.platform


class Homepage(SingletonModel):
    about_me = models.TextField(verbose_name='About Me section', blank=True, help_text='Write in Markdown format')
    skills = models.TextField(verbose_name='My Skills section', blank=True, help_text='Write in Markdown format')
    resume = models.FileField(blank=True, help_text='Upload resume as a PDF for best compatibility')

    def delete(self, *args, **kwargs):
        # Delete the file if it exists
        try:
            storage, path = self.resume.storage, self.resume.path
            storage.delete(path)
        except ValueError:
            pass
        # Delete the model
        super(Homepage, self).delete(*args, **kwargs)


# delete old upload on save
@receiver(models.signals.pre_save)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if isinstance(instance, Homepage):
        # check instance existence
        if not instance.pk:
            return False
        # get old file
        try:
            old_file = sender.objects.get(pk=instance.pk).resume
            # get new file
            new_file = instance.resume
            # remove if files are changed
            if old_file != new_file and os.path.isfile(old_file.path):
                os.remove(old_file.path)
        except (ValueError, Homepage.DoesNotExist):
            return False
