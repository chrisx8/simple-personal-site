from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import ProjectsConfig, Project

admin.site.register(ProjectsConfig, SingletonModelAdmin)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'posted']
    list_filter = ['posted']
    readonly_fields = ["id", "posted"]
