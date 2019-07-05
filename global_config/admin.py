from django.contrib import admin
from django.contrib.auth.models import Group
from global_config.forms import AuthFormCaptcha, EmailConfigAdminForm
from global_config.site_config import SITE_NAME
from solo.admin import SingletonModelAdmin
from .models import SiteInfo, EmailConfig, Fathom, GoogleAnalytics, SocialMediaLink

# Customize admin page
# set admin site title
admin.site.site_title = SITE_NAME
admin.site.site_header = 'Admin Panel // ' + SITE_NAME

# admin login form with captcha
admin.site.login_form = AuthFormCaptcha
admin.site.login_template = 'login.html'
admin.site.logout_template = 'logout.html'

# remove auth group
admin.site.unregister(Group)

# register global config models
admin.site.register(Fathom, SingletonModelAdmin)
admin.site.register(GoogleAnalytics, SingletonModelAdmin)


@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    ordering = ['platform']
    list_display = ['platform', 'username']


@admin.register(SiteInfo)
class SiteInfoAdmin(SingletonModelAdmin):
    fieldsets = (
        ('Basic Info', {'fields': ['site_name', 'site_url', 'description']}),
        ('Header', {'fields': ['header_title', 'header_subtitle']}),
        ('Footer', {'fields': ['footer_copyright']}),
    )


@admin.register(EmailConfig)
class EmailConfigAdmin(SingletonModelAdmin):
    form = EmailConfigAdminForm
