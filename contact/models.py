from django.db import models


class ContactConfig(models.Model):
    hcaptcha_site_key = models.UUIDField(null=True, blank=True, verbose_name='hCaptcha Sitekey',
                                         help_text='Leaving blank = no captcha on contact form')
    hcaptcha_secret_key = models.CharField(max_length=42, blank=True, verbose_name='hCaptcha secret key',
                                         help_text='Leaving blank = no captcha on contact form')
    site_owner_email = models.EmailField(blank=True, verbose_name='Site owner\'s email address.',
                                         help_text='Leaving blank = no notification emails to site owner')
    from_name = models.CharField(max_length=50, blank=True, verbose_name='Name shown on outgoing emails',
                                 help_text='Leaving blank = no emails')
    from_email = models.EmailField(blank=True, verbose_name='Email address shown on outgoing emails',
                                   help_text='Leaving blank = no emails')
    subject = models.CharField(max_length=250, blank=True, verbose_name='Subject of outgoing emails',
                               help_text='Leaving blank = no emails to message sender')
    pgp_fingerprint = models.CharField(max_length=50, blank=True, verbose_name='Public key fingerprint')
    pgp_url = models.URLField(blank=True, verbose_name='Public key URL')

    class Meta:
        verbose_name = '# Contact Config #'


# contact form
class Message(models.Model):
    name = models.CharField(max_length=100, default='', null=False)
    email = models.EmailField(null=False)
    message = models.TextField(null=False, default='')
    read = models.BooleanField(null=False, default=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        ordering = ['read', 'timestamp']

    def __str__(self):
        return self.name
