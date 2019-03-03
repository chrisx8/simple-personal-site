from django.db import models
from media.models import Image, Video


class Article(models.Model):
	title = models.CharField(max_length=100, default='', null=False)
	subtitle = models.CharField(max_length=100, default='', null=False, blank=True)
	images = models.ManyToManyField(Image, blank=True,
									help_text="When both image and video are selected, only video will show.")
	video = models.ForeignKey(Video, blank=True, null=True, on_delete=models.CASCADE,
							  help_text="When both image and video are selected, only video will show.")
	content = models.TextField(default='', null=False, help_text='Write in Markdown')
	show = models.BooleanField(default=True, null=False, help_text='Show article on blog')
	time_posted = models.DateField(auto_now_add=True)
	last_edited = models.DateField(auto_now=True)

	def __str__(self):
		return self.title
