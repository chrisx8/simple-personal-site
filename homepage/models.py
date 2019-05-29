import os
from django.db import models
from django.dispatch import receiver
from solo.models import SingletonModel


class Homepage(SingletonModel):
    about_me = models.TextField(verbose_name='About Me section', blank=True, help_text='Write in Markdown format')
    resume = models.FileField(blank=True, help_text='Upload resume as a PDF for best compatibility')

    def delete(self, *args, **kwargs):
        # Delete the file if it exists
        try:
            storage, path = self.resume.storage, self.resume.path
            storage.delete(path)
        except ValueError:
            pass
        # Delete the model
        super(Homepage, self).delete(*args, **kwargs)


# delete old upload on save
@receiver(models.signals.pre_save)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if isinstance(instance, Homepage):
        # check instance existence
        if not instance.pk:
            return False
        # get old file
        try:
            old_file = sender.objects.get(pk=instance.pk).resume
            # get new file
            new_file = instance.resume
            # remove if files are changed
            if old_file != new_file and os.path.isfile(old_file.path):
                os.remove(old_file.path)
        except:
            return False
