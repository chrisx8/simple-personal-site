from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import ContactConfig, Message

admin.site.register(ContactConfig, SingletonModelAdmin)


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
    readonly_fields = ["name", "email", "message", "timestamp"]
    actions = [mark_read, mark_unread]
