from django.contrib import admin
from .models import Embed, Image

admin.site.register(Embed)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    # delete objects and uploaded files
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()
