from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from media.models import Embed, Image


class BlogConfig(models.Model):
    articles_per_page = models.IntegerField(blank=False, default=10)

    class Meta:
        verbose_name = '# Blog Config #'


class Tag(models.Model):
    tag = models.CharField(max_length=50, default='', null=False, primary_key=True)

    class Meta:
        ordering = ['tag']

    def get_absolute_url(self):
        return reverse('filter_by_tag', kwargs={'tag': self.tag})

    def __str__(self):
        return self.tag


class Article(models.Model):
    id = models.SlugField(primary_key=True, verbose_name='Article ID')
    title = models.CharField(max_length=250, default='', null=False, unique=True)
    subtitle = models.CharField(max_length=250, default='', null=False, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.CASCADE,
                              help_text="<strong>When printing, only image will show.</strong><br>"
                                        "If both are selected, only embedded media will show on screen.")
    embed = models.ForeignKey(Embed, blank=True, null=True, on_delete=models.CASCADE,
                              help_text="<strong>When printing, only image will show.</strong><br>"
                                        "If both are selected, only embedded media will show on screen.")
    content = models.TextField(default='', null=False, help_text='Write in Markdown')
    last_edited = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-last_edited', 'title']

    def get_absolute_url(self):
        return reverse('view_article', kwargs={'id': self.id})

    def save(self):
        old_id = self.id
        # slugify title, get first 250 characters
        new_id = slugify(self.title)[:250]
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
