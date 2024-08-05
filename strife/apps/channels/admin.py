from django.contrib import admin

from .models import Messageable


@admin.register(Messageable)
class MessageableAdmin(admin.ModelAdmin):
    list_display = ("name", "server")
    ordering = ("created_at",)
    search_fields = ("name",)
    autocomplete_fields = ("server",)
    save_as = True
