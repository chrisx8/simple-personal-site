from django.db import models


class ContactConfig(models.Model):
    site_owner_email = models.EmailField(blank=True, verbose_name='Site owner\'s email address.',
                                         help_text='Leaving blank disables notification emails to site owner')
    from_name = models.CharField(max_length=50, blank=True, verbose_name='Name shown on outgoing emails.',
                                 help_text='Leaving blank disables emails to message sender')
    from_email = models.EmailField(blank=True, verbose_name='Email address shown on outgoing emails.',
                                   help_text='Leaving blank disables emails to message sender')

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
