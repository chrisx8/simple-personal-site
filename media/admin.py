from django.contrib import admin
from .models import Image, Video

admin.site.register(Video)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    # delete objects and uploaded files
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()
