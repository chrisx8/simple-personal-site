import os
from django.db import models
from django.dispatch import receiver


class Image(models.Model):
	image = models.ImageField(upload_to='blog', null=False)
	caption = models.CharField(max_length=50, default='', null=False, blank=True)

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


class Article(models.Model):
	title = models.CharField(max_length=100, default='', null=False)
	subtitle = models.CharField(max_length=100, default='', null=False, blank=True)
	images = models.ManyToManyField(Image, blank=True)
	content = models.TextField(default='', null=False, help_text='Write in Markdown')
	show = models.BooleanField(default=True, null=False, help_text='Show article on blog')
	time_posted = models.DateTimeField(auto_now_add=True)
	last_edited = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


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
