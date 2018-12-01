from django.contrib import admin

from .models import Homepage


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    ordering = ['-id']
