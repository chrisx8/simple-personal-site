import os
from django.db import models
from django.dispatch import receiver


class Image(models.Model):
    image = models.ImageField(verbose_name='Image', blank=False)
    caption = models.CharField(max_length=50, blank=True)

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


class Video(models.Model):
    VIDEO_SOURCE_CHOICES = (
        ('youtube', 'YouTube'),
        ('vimeo', 'Vimeo'),
    )
    BASE_URLS = {
        'youtube': 'https://www.youtube-nocookie.com/embed/',
        'vimeo': 'https://player.vimeo.com/video/',
    }
    name = models.CharField(max_length=50, blank=False, default='')
    video_source = models.CharField(max_length=10, blank=False, default='', choices=VIDEO_SOURCE_CHOICES)
    video_id = models.CharField(max_length=15, blank=False, default='',
                                help_text='YouTube video ID is the 11-character string after "watch?v=". '
                                          'Vimeo video ID is the numbers after "vimeo.com/"')

    def embed_url(self):
        return self.BASE_URLS[str(self.video_source)] + str(self.video_id)

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
