from django.contrib import admin

from .models import Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "server", "created_at", "member_count")
    ordering = ("created_at",)
    search_fields = ("name", "server")
    autocomplete_fields = ("server",)
    save_as = True

    def member_count(self, obj):
        return obj.members.count()
