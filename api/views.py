from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from games.models import Game, Publisher
from reviews.models import Review
from .serializers import GameSerializer, PublisherSerializer, ReviewSerializer


class GameApiListView(ListAPIView):
    queryset = Game.objects.select_related("publisher").all()
    serializer_class = GameSerializer
    permission_classes = [AllowAny]


class GameApiDetailView(RetrieveAPIView):
    queryset = Game.objects.select_related("publisher").all()
    serializer_class = GameSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"


class PublisherApiListView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [AllowAny]


class ReviewApiListView(ListAPIView):
    queryset = Review.objects.select_related("author", "game").all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]