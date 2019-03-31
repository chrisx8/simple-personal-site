from django.db import models
from django.urls import reverse
from media.models import Image, Video


class Tag(models.Model):
	tag = models.CharField(max_length=50, default='', null=False, primary_key=True)

	def get_absolute_url(self):
		return reverse('view_article', kwargs={'tag': self.tag})

	def __str__(self):
		return self.tag


class Article(models.Model):
	title = models.CharField(max_length=100, default='', null=False)
	subtitle = models.CharField(max_length=100, default='', null=False, blank=True)
	image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.CASCADE,
							  help_text="When both image and video are selected, only video will show.")
	video = models.ForeignKey(Video, blank=True, null=True, on_delete=models.CASCADE,
							  help_text="When both image and video are selected, only video will show.")
	content = models.TextField(default='', null=False, help_text='Write in Markdown')
	tag = models.ManyToManyField(Tag, blank=True)
	show = models.BooleanField(default=True, null=False, help_text='Show article on blog')
	time_posted = models.DateField(auto_now_add=True)
	last_edited = models.DateField(auto_now=True)

	def get_absolute_url(self):
		return reverse('view_article', kwargs={'id': self.id})

	def __str__(self):
		return self.title
