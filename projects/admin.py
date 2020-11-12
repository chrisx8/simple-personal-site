from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import ProjectsConfig, Project

admin.site.register(ProjectsConfig, SingletonModelAdmin)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Project Info', {'fields': ['order', 'title', 'description']}),
        ('Media', {'fields': ['image', 'embed']}),
        ('URL', {'fields': ['url']}),
    )
    list_display = ['title', 'order']
    readonly_fields = ["id"]
