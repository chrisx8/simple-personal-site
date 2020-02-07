import os
from django.db import models
from django.dispatch import receiver


class Image(models.Model):
    image = models.ImageField(verbose_name='Image', blank=False)

    class Meta:
        ordering = ['image']

    def delete(self, *args, **kwargs):
        # Delete the file if it exists
        try:
            storage, path = self.image.storage, self.image.path
            storage.delete(path)
        except ValueError:
            pass
        # Delete the model
        super(Image, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.image)


class Embed(models.Model):
    name = models.CharField(max_length=50, primary_key=True, blank=False, default='')
    embed_url = models.URLField(blank=False, default='', verbose_name='Embed URL',
                                help_text='Enter the EMBED URL, not the URL to a webpage.')

    class Meta:
        ordering = ['name']

    def html(self):
        return f'<div class="embed"><iframe class="frame" title="{self.name}" src="{self.embed_url}"' + \
               'frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></div>'

    def __str__(self):
        return self.name


# delete old upload on save
@receiver(models.signals.pre_save)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if isinstance(instance, Image):
        # check instance existence
        if not instance.pk:
            return False
        # get old file
        try:
            old_file = sender.objects.get(pk=instance.pk).image
            # get new file
            new_file = instance.image
            # remove if files are changed
            if old_file != new_file and os.path.isfile(old_file.path):
                os.remove(old_file.path)
        except:
            return False
