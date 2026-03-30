from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("game", "author", "rating", "created_at")
    list_filter = ("rating", "created_at", "author")
    search_fields = ("author__username", "author__nickname", "game__title", "text")