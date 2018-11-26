from django.contrib import admin
from simple_personal_site.site_config import SITE_NAME
from .models import Message

# set admin site titles
admin.site.site_title = SITE_NAME
admin.site.site_header = SITE_NAME

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'read','timestamp')
    list_filter = ('read', 'timestamp')
