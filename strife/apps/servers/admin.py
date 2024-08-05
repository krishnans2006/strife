from django.contrib import admin

from .models import Server


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "owner", "created_at")
    ordering = ("created_at",)
    search_fields = ("name", "description")
    autocomplete_fields = ("owner",)
    save_as = True
