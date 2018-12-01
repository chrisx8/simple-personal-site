from django.contrib import admin
from projects.models import Project
from .models import Homepage


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "featured_projects":
            kwargs["queryset"] = Project.objects.filter(show=True)
        return super(HomepageAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    ordering = ['-id']
