from django.contrib import admin
from .models import Article, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Article Info', {'fields': ['title', 'subtitle', 'tag', 'article_id', 'last_edited']}),
        ('Media', {'fields': ['image', 'embed']}),
        ('Content', {'fields': ['content']})
    )
    filter_horizontal = [('tag')]
    list_display = ['title', 'last_edited']
    list_filter = ['last_edited', 'tag']
    readonly_fields = ["article_id", "last_edited"]
    search_fields = ['title', 'subtitle', 'tag__tag', 'content']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['tag']
