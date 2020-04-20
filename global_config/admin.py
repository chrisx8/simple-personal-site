from django.contrib import admin
from django.contrib.auth.models import Group
from global_config.forms import AuthForm
from global_config.site_config import SITE_NAME
from solo.admin import SingletonModelAdmin
from .models import SiteInfo, Fathom, GoogleAnalytics, SocialMediaLink

# Customize admin page
# set admin site title
admin.site.site_title = SITE_NAME
admin.site.site_header = 'Admin Panel // ' + SITE_NAME

# remove auth group
admin.site.unregister(Group)

# register global config models
admin.site.register(Fathom, SingletonModelAdmin)
admin.site.register(GoogleAnalytics, SingletonModelAdmin)


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
