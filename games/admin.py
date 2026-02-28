from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Game, Genre


@admin.register(Genre)
class GenreAdmin(ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Game)
class GameAdmin(ModelAdmin):
    list_display = (
        "title",
        "min_players",
        "max_players",
        "duration_min",
        "created_at",
    )
    list_filter = ("genres",)
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")