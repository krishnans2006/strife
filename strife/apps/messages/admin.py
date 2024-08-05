from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "channel", "created_at")
    ordering = ("created_at",)
    search_fields = ("content",)
    autocomplete_fields = ("author", "channel")
    save_as = True
