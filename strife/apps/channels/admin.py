from django.contrib import admin

from .models import ForumChannel, Messageable, Speakable, StageChannel, TextChannel, VoiceChannel


@admin.register(Messageable)
@admin.register(TextChannel)
@admin.register(ForumChannel)
class MessageableAdmin(admin.ModelAdmin):
    list_display = ("name", "server")
    ordering = ("created_at",)
    search_fields = ("name",)
    autocomplete_fields = ("server",)
    save_as = True


@admin.register(Speakable)
@admin.register(VoiceChannel)
@admin.register(StageChannel)
class SpeakableAdmin(admin.ModelAdmin):
    list_display = ("name", "server")
    ordering = ("created_at",)
    search_fields = ("name",)
    autocomplete_fields = ("server",)
    save_as = True
