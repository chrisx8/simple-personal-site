import os
from django.db import models
from django.dispatch import receiver


class Project(models.Model):
    title = models.CharField(verbose_name='Project Name', max_length=100, default='', null=False)
    description = models.TextField(verbose_name='Project Description', default='', null=False)
    image = models.FileField(verbose_name='Project Image', upload_to='projects', blank=True)
    youtube_id = models.CharField(verbose_name='Youtube Video ID', max_length=15, blank=True,
                                  help_text='Video ID is the 11-character string after ?v=. For example, if your '
                                            'YouTube video URL is https://www.youtube.com/watch?v=dQw4w9WgXcQ, '
                                            'the Video ID is dQw4w9WgXcQ')
    url = models.URLField(verbose_name='Project URL', null=False, default='')
    url_description = models.CharField(verbose_name='URL Description', max_length=50, default='Website', null=False)
    fa_icon = models.CharField(verbose_name='Font Awesome icon class', max_length=50, default='', 
                               null=False, blank=True)
    show = models.BooleanField(verbose_name='Show on Projects page', default=True, null=False)

    def delete(self, *args, **kwargs):
        # Delete the file if it exists
        try:
            storage, path = self.image.storage, self.image.path
            storage.delete(path)
        except ValueError:
            pass
        # Delete the model
        super(Project, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title


# delete old upload on save
@receiver(models.signals.pre_save)
def auto_delete_file_on_change(sender, instance, **kwargs):
    # check instance existence
    if not instance.pk:
        return False
    # get old file
    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False
    # get new file
    new_file = instance.image
    # remove if files are changed
    if old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
