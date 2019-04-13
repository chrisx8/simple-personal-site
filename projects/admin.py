from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # delete objects and uploaded files
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

    list_display = ['title', 'posted']
    list_filter = ['posted']
    readonly_fields = ["id", "posted"]
