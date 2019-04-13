from django.db import models


class Homepage(models.Model):
    about_me = models.TextField(verbose_name='About Me section', default='', null=False,
                                help_text='Write in Markdown format')
    resume = models.FileField(blank=True, help_text='Upload resume as a PDF for best compatibility')

    class Meta:
        ordering = ['-id']

    def delete(self, *args, **kwargs):
        # Delete the file if it exists
        try:
            storage, path = self.resume.storage, self.resume.path
            storage.delete(path)
        except ValueError:
            pass
        # Delete the model
        super(Homepage, self).delete(*args, **kwargs)
