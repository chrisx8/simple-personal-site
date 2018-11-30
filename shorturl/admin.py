from django.contrib import admin
from .models import ShortURL


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    # enable selected short urls
    def enable_url(self, request, queryset):
        queryset.update(enabled=True)

    # disable selected short urls
    def disable_url(self, request, queryset):
        queryset.update(enabled=False)

    enable_url.short_description = 'Enable selected short urls'
    disable_url.short_description = 'Disable selected short urls'

    list_display = ['alias', 'full_url', 'enabled']
    list_filter = ['enabled']
    actions = [enable_url, disable_url]
