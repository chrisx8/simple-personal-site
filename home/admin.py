from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Homepage, SiteInfo, SocialMediaLink

admin.site.register(Homepage, SingletonModelAdmin)


@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ["platform", "url"]
    search_fields = ["platform", "url"]


@admin.register(SiteInfo)
class SiteInfoAdmin(SingletonModelAdmin):
    fieldsets = (
        ("Basic Info", {"fields": ["site_name", "site_url", "description"]}),
        ("Header", {"fields": ["header_title", "header_subtitle"]}),
        ("Footer", {"fields": ["footer_copyright"]}),
    )
