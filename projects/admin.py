from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # show selected on projects page
    def show_projects(self, request, queryset):
        queryset.update(show=True)

    # hide selected on projects page
    def hide_projects(self, request, queryset):
        queryset.update(show=False)

    # delete objects and uploaded files
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

    show_projects.short_description = 'Show selected projects on Projects page'
    hide_projects.short_description = 'Hide selected projects on Projects page'

    ordering = ['title']
    list_display = ['title', 'show']
    list_filter = ['show']
    actions = [show_projects, hide_projects]
