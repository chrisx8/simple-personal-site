import django.contrib.auth.models as auth_models
from django.contrib import admin
from simple_personal_site.forms import AuthFormCaptcha
from simple_personal_site.site_config import SITE_NAME
from .models import Message, SocialMediaLink

# Customize admin page
# set admin site title
admin.site.site_title = SITE_NAME
admin.site.site_header = SITE_NAME

# admin login form with captcha
admin.site.login_form = AuthFormCaptcha
admin.site.login_template = 'login.html'
admin.site.logout_template = 'logout.html'

# remove unnecessary features
admin.site.unregister(auth_models.Group)
admin.site.unregister(auth_models.User)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    # mark selected as read
    def mark_read(self, request, queryset):
        queryset.update(read=True)

    # mark selected as unread
    def mark_unread(self, request, queryset):
        queryset.update(read=False)

    mark_read.short_description = 'Mark selected messages as read'
    mark_unread.short_description = 'Mark selected messages as unread'

    ordering = ['read', 'timestamp', 'name']
    list_display = ['name', 'email', 'read', 'timestamp']
    list_filter = ['read', 'timestamp']
    actions = [mark_read, mark_unread]


@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    # show selected on home/contact page
    def show(self, request, queryset):
        queryset.update(show=True)

    # hide selected on home/contact page
    def hide(self, request, queryset):
        queryset.update(show=False)

    show.short_description = 'Show selected social media links on Projects page'
    show.short_description = 'Hide selected social media links on Projects page'

    ordering = ['platform']
    list_display = ['platform', 'username', 'show']
    list_filter = ['show']
    actions = [show, hide]
