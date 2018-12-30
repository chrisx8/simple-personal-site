from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=100, default='', null=False)
	subtitle = models.CharField(max_length=100, default='', null=False, blank=True)
	content = models.TextField(default='', null=False, help_text='Write in Markdown')
	show = models.BooleanField(default=True, null=False, help_text='Show article on blog')
	time_posted = models.DateTimeField(auto_now_add=True)
	last_edited = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
