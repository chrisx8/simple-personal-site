from django.db import models
from solo.models import SingletonModel


class ContactConfig(SingletonModel):
    hcaptcha_site_key = models.UUIDField(null=True, blank=True, verbose_name='hCaptcha Sitekey',
                                         help_text='Blank = no captcha on contact form')
    hcaptcha_secret_key = models.CharField(max_length=42, blank=True, verbose_name='hCaptcha secret key',
                                         help_text='Blank = no captcha on contact form')
    from_email = models.EmailField(blank=True, verbose_name='Email address shown on outgoing emails',
                                   help_text='Blank = no outgoing emails')
    notification_recipient = models.EmailField(blank=True, verbose_name='Notification recipient\'s email address',
                                               help_text='Blank = no notification emails for new messages')

    class Meta:
        verbose_name = '*Contact Config*'


# contact form
class Message(models.Model):
    name = models.CharField(max_length=100, default='', blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=300, default='(no subject)', blank=False)
    message = models.TextField(blank=False, default='')
    timestamp = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        ordering = ['-timestamp']

    def save(self):
        # override subject if it's blank
        if not self.subject:
            self.subject = '(no subject)'
        super().save(self)

    def __str__(self):
        return self.subject
