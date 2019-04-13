from django.db import models


# contact info
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


# social media links
class SocialMediaLink(models.Model):
    platform = models.CharField(max_length=50, default='', null=False, help_text='Name of the social media platform')
    username = models.CharField(max_length=100, default='', null=False, help_text='Omit @ symbol')
    url = models.URLField(default='', null=False, help_text='Link to profile page')
    color = models.CharField(max_length=6, default='3273DC', null=False, help_text='Color of social media logo.')
    fa_icon = models.CharField(verbose_name='Font Awesome icon class', max_length=50, default='',
                               null=False, blank=True)
    display_at = models.BooleanField(verbose_name='Display "@" before username', default=False, null=False)

    class Meta:
        ordering = ['platform', 'username']

    def __str__(self):
        if self.display_at:
            return f'{self.platform} @{self.username}'
        else:
            return f'{self.platform} - {self.username}'
