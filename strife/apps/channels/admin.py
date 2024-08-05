from django.contrib import admin

from .models import Messageable, Speakable, TextChannel, ForumChannel, VoiceChannel, StageChannel


@admin.register(Messageable)
class MessageableAdmin(admin.ModelAdmin):
    list_display = ("name", "server")
    ordering = ("created_at",)
    search_fields = ("name",)
    autocomplete_fields = ("server",)
    save_as = True


@admin.register(Speakable)
class SpeakableAdmin(admin.ModelAdmin):
    list_display = ("name", "server")
    ordering = ("created_at",)
    search_fields = ("name",)
    autocomplete_fields = ("server",)
    save_as = True


@admin.register(TextChannel)
class TextChannelAdmin(admin.ModelAdmin):
    list_display = ("name", "server")
    ordering = ("created_at",)
    search_fields = ("name",)
    autocomplete_fields = ("server",)
    save_as = True


@admin.register(ForumChannel)
class ForumChannelAdmin(admin.ModelAdmin):
    list_display = ("name", "server")
    ordering = ("created_at",)
    search_fields = ("name",)
    autocomplete_fields = ("server",)
    save_as = True


@admin.register(VoiceChannel)
class VoiceChannelAdmin(admin.ModelAdmin):
    list_display = ("name", "server")
    ordering = ("created_at",)
    search_fields = ("name",)
    autocomplete_fields = ("server",)
    save_as = True


@admin.register(StageChannel)
class StageChannelAdmin(admin.ModelAdmin):
    list_display = ("name", "server")
    ordering = ("created_at",)
    search_fields = ("name",)
    autocomplete_fields = ("server",)
    save_as = True
