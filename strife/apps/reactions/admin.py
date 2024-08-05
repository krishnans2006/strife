from django.contrib import admin

from .models import Reaction


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "message", "emoji")
    ordering = ("created_at",)
    search_fields = ("user", "message", "emoji")
    autocomplete_fields = ("user", "message", "emoji")
    save_as = True
