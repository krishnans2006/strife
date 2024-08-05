from django.contrib import admin

from .models import Emoji


@admin.register(Emoji)
class EmojiAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at")
    ordering = ("created_at",)
    search_fields = ("name",)
    save_as = True
