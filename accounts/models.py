from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nickname = models.CharField(
        max_length=30,
        unique=True,
        validators=[MinLengthValidator(2)],
        help_text="Enter a nickname between 2 and 30 characters.",
    )
    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )
    played_games = models.ManyToManyField(
        "games.Game",
        related_name="played_by_users",
        blank=True,
    )
    wishlist_games = models.ManyToManyField(
        "games.Game",
        related_name="wishlisted_by_users",
        blank=True,
    )

    def __str__(self):
        return self.username