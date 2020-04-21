from django.contrib import admin
from django.contrib.auth.models import Group
from global_config.forms import AuthForm
from django.db.utils import OperationalError
from solo.admin import SingletonModelAdmin
from .models import SiteInfo, Fathom, GoogleAnalytics, SocialMediaLink

# set admin site title
try:
    site_info = SiteInfo.objects.get_or_create()[0]
    admin.site.site_title = site_info.site_name
    admin.site.site_header = 'Admin Panel // ' + site_info.site_name
except OperationalError:
    pass

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
