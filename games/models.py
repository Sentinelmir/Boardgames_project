from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.text import slugify

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name)
            self.slug = base or "genre"
        super().save(*args, **kwargs)


class Game(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    description = models.TextField()

    min_players = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        help_text="Minimum number of players.",
    )
    max_players = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        help_text="Maximum number of players.",
    )

    duration_min = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        help_text="Average playtime in minutes.",
    )

    age_min = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99)],
        blank=True,
        null=True,
        help_text="Minimum recommended age (optional).",
    )

    image = models.ImageField(
        upload_to="games/",
        blank=True,
        null=True,
        help_text="Square image looks best.",
    )

    genres = models.ManyToManyField(
        Genre,
        related_name="games",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title

    def clean(self):
        super().clean()
        if self.min_players and self.max_players and self.min_players > self.max_players:
            raise ValidationError({"max_players": "Max players must be >= min players."})

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            self.slug = base or "game"
        super().save(*args, **kwargs)