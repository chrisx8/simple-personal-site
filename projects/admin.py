from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Project Info', {'fields': ['order', 'title', 'description']}),
        ('Media', {'fields': ['image', 'embed']}),
        ('URL', {'fields': ['url']}),
    )
    list_display = ['title', 'order']
