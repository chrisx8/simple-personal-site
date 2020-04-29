from django.contrib import admin
from django.db.utils import OperationalError
from solo.admin import SingletonModelAdmin
from .models import Homepage, SiteInfo, SocialMediaLink

# set admin site title
admin.site.index_title = "Admin Panel"
try:
    site_info = SiteInfo.objects.get_or_create()[0]
    admin.site.site_title = site_info.site_name
    admin.site.site_header = site_info.site_name
except OperationalError:
    pass

admin.site.register(Homepage, SingletonModelAdmin)


@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    ordering = ['platform']
    list_display = ['platform', 'url']


@admin.register(SiteInfo)
class SiteInfoAdmin(SingletonModelAdmin):
    fieldsets = (
        ('Basic Info', {'fields': ['site_name', 'site_url', 'description']}),
        ('Header', {'fields': ['header_title', 'header_subtitle']}),
        ('Footer', {'fields': ['footer_copyright']}),
    )

