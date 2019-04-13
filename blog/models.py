from django.db import models
from django.urls import reverse
from media.models import Image, Video
import string


class Tag(models.Model):
    tag = models.CharField(max_length=50, default='', null=False, primary_key=True)

    def get_absolute_url(self):
        return reverse('filter_by_tag', kwargs={'tag': self.tag})

    def __str__(self):
        return self.tag


class Article(models.Model):
    id = models.CharField(primary_key=True, max_length=100, verbose_name='Article ID')
    title = models.CharField(max_length=100, default='', null=False)
    subtitle = models.CharField(max_length=100, default='', null=False, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.CASCADE,
                              help_text="When both image and video are selected, only video will show.")
    video = models.ForeignKey(Video, blank=True, null=True, on_delete=models.CASCADE,
                              help_text="When both image and video are selected, only video will show.")
    content = models.TextField(default='', null=False, help_text='Write in Markdown')
    last_edited = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('view_article', kwargs={'id': self.id})

    def get_article_id(self):
        title = str(self.title).lower()
        article_id = ''
        # only include numbers and letters and replace space with -
        for char in title:
            if char in string.ascii_letters or char in string.digits:
                article_id += char
            elif char in string.whitespace:
                article_id += '-'
        return article_id

    def save(self):
        old_id = self.id
        new_id = self.get_article_id()
        # delete old if id changed
        if old_id != new_id:
            self.id = new_id
            try:
                Article.delete(Article.objects.get(id=old_id))
            except self.DoesNotExist:
                pass
        super(Article, self).save()

    def __str__(self):
        return self.title
