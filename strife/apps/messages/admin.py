from django.contrib import admin

from .models import Attachment, Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "channel", "created_at", "is_edited")
    ordering = ("created_at",)
    search_fields = ("content",)
    autocomplete_fields = ("author", "channel")
    save_as = True


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("id", "message", "file")
    ordering = ("message__created_at",)
    search_fields = ("message__content", "file")
    autocomplete_fields = ("message",)
    save_as = True
