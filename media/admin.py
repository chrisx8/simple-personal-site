from django.contrib import admin

from .models import Embed, Image


@admin.register(Embed)
class EmbedAdmin(admin.ModelAdmin):
    search_fields = ["name", "embed_url"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    search_fields = ["image"]

    # delete objects and uploaded files
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()
