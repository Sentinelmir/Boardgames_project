from rest_framework import serializers
from games.models import Game, Publisher
from reviews.models import Review


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["id", "name", "slug", "website", "description"]


class GameSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer(read_only=True)
    average_rating = serializers.ReadOnlyField()

    class Meta:
        model = Game
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "publisher",
            "genres",
            "min_players",
            "max_players",
            "duration_min",
            "age_min",
            "average_rating",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    game = serializers.SlugRelatedField(read_only=True, slug_field="slug")

    class Meta:
        model = Review
        fields = ["id", "game", "author", "rating", "text", "created_at"]