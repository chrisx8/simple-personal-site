from django.contrib import admin
from .models import Article, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'last_edited']
    list_filter = ['last_edited']
    readonly_fields = ["id", "last_edited"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']
