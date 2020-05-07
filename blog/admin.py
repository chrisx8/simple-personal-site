from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Article, BlogConfig, Tag

admin.site.register(BlogConfig, SingletonModelAdmin)
admin.site.register(Tag)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Article Info', {'fields': ['title', 'subtitle', 'tag', 'id', 'last_edited']}),
        ('Media', {'fields': ['image', 'embed']}),
        ('Content', {'fields': ['content']})
    )
    filter_horizontal = [('tag')]
    list_display = ['title', 'last_edited']
    list_filter = ['last_edited']
    readonly_fields = ["id", "last_edited"]
