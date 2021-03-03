from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import ContactConfig, Message


@admin.register(ContactConfig)
class ContactConfigAdmin(SingletonModelAdmin):
    fieldsets = (
        ('hCaptcha on contact form', {'fields': ['hcaptcha_site_key', 'hcaptcha_secret_key']}),
        ('Email Config', {'fields': ['from_email', 'notification_recipient']}),
        ('PGP Public Key', {'fields': ['pgp_fingerprint', 'pgp_key']})
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    list_display = ['subject', 'name', 'timestamp']
    list_filter = ['timestamp']
    readonly_fields = ['name', 'email', 'subject', 'message', 'timestamp']
    fieldsets = (
        ('Information', {'fields': ['name', 'email', 'timestamp']}),
        ('Message Content', {'fields': ['subject', 'message']}),
    )
