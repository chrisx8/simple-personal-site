from django.contrib import admin
from django.db import models
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
    
    def save(self):
        admin.site.site_title = self.site_name
        admin.site.site_header = 'Admin Panel // ' + self.site_name
        super(SiteInfo, self).save()


class Fathom(SingletonModel):
    fathom_url = models.URLField(blank=True, verbose_name='Fathom URL', help_text='Full URL to Fathom\'s "tracker.js". '
                                                                                  'Leaving blank disables Fathom.')
    site_id = models.CharField(max_length=5, blank=True, verbose_name='Site ID',
                               help_text='Fathom Site ID. Leaving blank disables Fathom')

    class Meta:
        verbose_name = 'Fathom Analytics'


class GoogleAnalytics(SingletonModel):
    ga_tracking_id = models.CharField(max_length=15, blank=True, verbose_name='Tracking ID',
                                      help_text='Google Analytics Tracking ID. Leaving blank disables Google Analytics')

    class Meta:
        verbose_name = 'Google Analytics'


class SocialMediaLink(models.Model):
    platform = models.CharField(max_length=50, default='', null=False, help_text='Name of the social media platform')
    url = models.URLField(default='', null=False, verbose_name='URL', help_text='Link to profile page')

    class Meta:
        ordering = ['platform']
        verbose_name = 'Social Media Link'

    def __str__(self):
        return self.platform
