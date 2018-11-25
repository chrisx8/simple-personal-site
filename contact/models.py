from django.db import models


# contact info
class Message(models.Model):
    name = models.CharField(max_length=100, default='', null=False)
    email = models.EmailField(null=False)
    message = models.TextField(null=False, default='')
    read = models.BooleanField(null=False, default=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=False)

    # Metadata
    class Meta: 
        ordering = ['read', 'timestamp']

    def __str__(self):
        return self.name
