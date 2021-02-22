from django.db import models


class ContactConfig(models.Model):
    hcaptcha_site_key = models.UUIDField(null=True, blank=True, verbose_name='hCaptcha Sitekey',
                                         help_text='Blank = no captcha on contact form')
    hcaptcha_secret_key = models.CharField(max_length=42, blank=True, verbose_name='hCaptcha secret key',
                                         help_text='Blank = no captcha on contact form')
    from_email = models.EmailField(blank=True, verbose_name='Email address shown on outgoing emails',
                                   help_text='Blank = no outgoing emails')
    notification_recipient = models.EmailField(blank=True, verbose_name='Notification recipient\'s email address',
                                               help_text='Blank = no notification emails for new messages')
    pgp_fingerprint = models.CharField(max_length=50, blank=True, verbose_name='Public key fingerprint')
    pgp_key = models.TextField(blank=True, verbose_name='Public key', 
                               help_text='Begins with "-----BEGIN PGP PUBLIC KEY BLOCK-----"')

    class Meta:
        verbose_name = '*Contact Config*'


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
