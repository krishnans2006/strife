from django.contrib import admin

from .models import Server, Member, Owner


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "owner", "created_at")
    ordering = ("created_at",)
    search_fields = ("name", "description")
    autocomplete_fields = ("owner",)
    save_as = True


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("user", "server", "nickname", "joined_at")
    ordering = ("joined_at",)
    search_fields = ("user", "server")
    autocomplete_fields = ("user", "server")
    save_as = True


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("user", "server", "updated_at")
    ordering = ("updated_at",)
    search_fields = ("user", "server")
    autocomplete_fields = ("user", "server")
    save_as = True
