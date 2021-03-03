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
    list_display = ['__str__', 'timestamp']
    list_filter = ['timestamp']
    readonly_fields = ['name', 'email', 'message', 'timestamp']
