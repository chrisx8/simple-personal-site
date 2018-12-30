from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # show selected
    def show(self, request, queryset):
        queryset.update(show=True)

    # hide selected
    def hide(self, request, queryset):
        queryset.update(show=False)

    # delete objects and uploaded files
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

    show.short_description = 'Show selected projects'
    hide.short_description = 'Hide selected projects'

    ordering = ['title']
    list_display = ['title', 'show']
    list_filter = ['show']
    actions = [show, hide]
