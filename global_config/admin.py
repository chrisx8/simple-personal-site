from django.contrib import admin
from django.contrib.auth.models import Group
from simple_personal_site.forms import AuthFormCaptcha
from solo.admin import SingletonModelAdmin
from .models import SiteInfo, ReCaptcha, GoogleAnalytics, Fathom, SocialMediaLink, EmailConfig

# Customize admin page
# set admin site title
admin.site.site_title = 'SITE_NAME'
admin.site.site_header = 'Admin Panel // ' + 'SITE_NAME'

# admin login form with captcha
admin.site.login_form = AuthFormCaptcha
admin.site.login_template = 'login.html'
admin.site.logout_template = 'logout.html'

# remove auth group
admin.site.unregister(Group)

# register global config models
admin.site.register(SiteInfo, SingletonModelAdmin)
admin.site.register(ReCaptcha, SingletonModelAdmin)
admin.site.register(GoogleAnalytics, SingletonModelAdmin)
admin.site.register(Fathom, SingletonModelAdmin)
admin.site.register(EmailConfig, SingletonModelAdmin)


@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    ordering = ['platform']
    list_display = ['platform', 'username']
