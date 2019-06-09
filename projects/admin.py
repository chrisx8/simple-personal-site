from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import ProjectsConfig, Project

admin.site.register(ProjectsConfig, SingletonModelAdmin)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Project Info', {'fields': ['title', 'description', 'posted']}),
        ('Media', {'fields': ['image', 'embed']}),
        ('URL', {'fields': ['url']}),
    )
    list_display = ['title', 'posted']
    list_filter = ['posted']
    readonly_fields = ["id", "posted"]
