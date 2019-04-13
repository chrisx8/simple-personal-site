from django.contrib import admin
from .models import Article, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # show selected article on blog
    def show(self, request, queryset):
        queryset.update(show=True)

    # hide selected article on blog
    def hide(self, request, queryset):
        queryset.update(show=False)

    show.short_description = 'Show selected articles'
    hide.short_description = 'Hide selected articles'

    ordering = ['-last_edited', 'title']
    list_display = ['title', 'last_edited']
    list_filter = ['last_edited']
    readonly_fields = ["id", "last_edited"]
    actions = [show, hide]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ordering = ['tag']
    list_display = ['tag']
