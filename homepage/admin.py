from django.contrib import admin
from .models import Homepage


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    # delete objects and uploaded files
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()
