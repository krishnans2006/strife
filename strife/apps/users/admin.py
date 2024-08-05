from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "display_name", "email", "created_at")
    ordering = ("created_at",)
    search_fields = ("username", "display_name", "email")
    save_as = True
