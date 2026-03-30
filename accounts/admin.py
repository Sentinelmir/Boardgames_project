from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ("username", "email", "nickname", "is_staff", "is_active", )
    list_filter = ("is_staff", "is_active", "is_superuser", "groups", )
    search_fields = ( "username", "email", "nickname", )
    ordering = ("username",)

    fieldsets = UserAdmin.fieldsets + (
        ("Profile info",
            {"fields": ("nickname", "profile_picture", "played_games", "wishlist_games", ) },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Profile info",
            {"fields": ("email", "nickname", "profile_picture", ) },
        ),
    )