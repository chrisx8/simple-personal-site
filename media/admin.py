from django.contrib import admin
from .models import Image, Video


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = ['image']

    # delete objects and uploaded files
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()


@admin.register(Video)
class ImageAdmin(admin.ModelAdmin):
    ordering = ['name']
