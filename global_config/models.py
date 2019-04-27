from django.db import models
from solo.models import SingletonModel


class SiteInfo(SingletonModel):
    site_name = models.CharField(max_length=50, default='My Site', blank=False)
    site_url = models.URLField(default='', blank=False, verbose_name='Site URL')
    # meta description
    description = models.CharField(max_length=250, default='', blank=True,
                                   help_text='This field sets the global Meta Description tag.')
    # site header on every page
    header_title = models.CharField(max_length=250, default='My Site', blank=False)
    header_subtitle = models.CharField(max_length=250, blank=True)
    # copyright footer on every page
    footer_copyright = models.CharField(max_length=250, default='Simple Personal Site by @chrisx8.',
                                        help_text='"&copy; year " always shows. Set this to be the text after '
                                                  '"&copy; year "')

    class Meta:
        verbose_name = '# Site Info #'


class ReCaptcha(SingletonModel):
    private_key = models.CharField(max_length=50, blank=True,
                                   help_text='Recommended for spam prevention. Leaving blank disables '
                                             'ReCaptcha. Get your ReCaptcha v2 key at '
                                             'https://www.google.com/recaptcha/admin')
    public_key = models.CharField(max_length=50, blank=True,
                                  help_text='Recommended for spam prevention. Leaving blank disables '
                                            'ReCaptcha. Get your ReCaptcha v2 key at '
                                            'https://www.google.com/recaptcha/admin')

    class Meta:
        verbose_name = 'ReCaptcha v2'


class GoogleAnalytics(SingletonModel):
    ga_tracking_id = models.CharField(max_length=15, blank=True, verbose_name='Tracking ID',
                                      help_text='Google Analytics Tracking ID. Leaving blank disables Google Analytics')

    class Meta:
        verbose_name = 'Google Analytics'


class Fathom(SingletonModel):
    fathom_url = models.URLField(blank=True, verbose_name='Fathom URL', help_text='Full URL to Fathom\'s "tracker.js". '
                                                                                  'Leaving blank disables Fathom.')
    site_id = models.CharField(max_length=5, blank=True, verbose_name='Site ID',
                               help_text='Fathom Site ID. Leaving blank disables Fathom')

    class Meta:
        verbose_name = 'Fathom Analytics'


class EmailConfig(SingletonModel):
    host = models.CharField(max_length=500, blank=True, help_text='URL to SMTP server. Leaving blank disables email.')
    port = models.IntegerField(blank=True, null=True, help_text='Port of SMTP server. Leaving blank disables email.')
    username = models.CharField(max_length=500, blank=True, help_text='SMTP username. Leaving blank disables email.')
    password = models.CharField(max_length=500, blank=True, help_text='SMTP password. Leaving blank disables email.')
    use_tls = models.BooleanField(default=False, verbose_name='Use TLS', help_text='Do not enable both SSL and TLS.')
    use_ssl = models.BooleanField(default=False, verbose_name='Use SSL', help_text='Do not enable both SSL and TLS.')

    class Meta:
        verbose_name = 'Email Config'


class SocialMediaLink(models.Model):
    platform = models.CharField(max_length=50, default='', null=False, help_text='Name of the social media platform')
    username = models.CharField(max_length=100, default='', null=False, help_text='Omit @ symbol')
    url = models.URLField(default='', null=False, help_text='Link to profile page')
    display_at = models.BooleanField(verbose_name='Display "@" before username', default=False, null=False)

    class Meta:
        ordering = ['platform', 'username']
        verbose_name = 'Social Media Link'

    def display_username(self):
        if self.display_at:
            return '@' + str(self.username)
        else:
            return self.username

    def __str__(self):
        if self.display_at:
            return f'{self.platform} @{self.username}'
        else:
            return f'{self.platform} - {self.username}'
