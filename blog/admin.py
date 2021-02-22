from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Article, Tag

admin.site.register(Tag)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Article Info', {'fields': ['title', 'subtitle', 'tag', 'article_id', 'last_edited']}),
        ('Media', {'fields': ['image', 'embed']}),
        ('Content', {'fields': ['content']})
    )
    filter_horizontal = [('tag')]
    list_display = ['title', 'last_edited']
    list_filter = ['last_edited']
    readonly_fields = ["article_id", "last_edited"]
