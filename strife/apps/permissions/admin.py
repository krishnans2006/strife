from django.contrib import admin

from .models import Permissions


@admin.register(Permissions)
class PermissionsAdmin(admin.ModelAdmin):
    list_display = ("id", "server_name", "role", "member")
    search_fields = ("server", "role", "member")
    save_as = True

    def server_name(self, obj):
        if obj.is_for_server:
            return obj.server.name
        if obj.is_for_member:
            return obj.member.server.name
        if obj.is_for_role:
            return obj.role.server.name
        return "Unassigned"
