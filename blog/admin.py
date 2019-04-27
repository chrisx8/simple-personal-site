from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Article, BlogConfig, Tag

admin.site.register(BlogConfig, SingletonModelAdmin)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'last_edited']
    list_filter = ['last_edited']
    readonly_fields = ["id", "last_edited"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']
