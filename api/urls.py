from django.urls import path
from .views import (
    GameApiListView,
    GameApiDetailView,
    PublisherApiListView,
    ReviewApiListView,
)

app_name = "api"

urlpatterns = [
    path("games/", GameApiListView.as_view(), name="games-list"),
    path("games/<slug:slug>/", GameApiDetailView.as_view(), name="games-detail"),
    path("publishers/", PublisherApiListView.as_view(), name="publishers-list"),
    path("reviews/", ReviewApiListView.as_view(), name="reviews-list"),
]