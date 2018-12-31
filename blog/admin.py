from django.contrib import admin
from .models import Article, Image


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

    ordering = ['-time_posted', 'title']
    list_display = ['title', 'time_posted', 'last_edited', 'show']
    list_filter = ['show']
    actions = [show, hide]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = ['image']

    # delete objects and uploaded files
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()
