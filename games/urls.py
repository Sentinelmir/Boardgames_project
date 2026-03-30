from django.urls import path
from .views import GameListView, GameDetailView, GameCreateView, GameUpdateView, GameDeleteView, PlayedView, WishlistView

app_name = "games"

urlpatterns = [
    path("", GameListView.as_view(), name="list"),
    path("create/", GameCreateView.as_view(), name="create"),
    path("<slug:slug>/", GameDetailView.as_view(), name="detail"),
    path("<slug:slug>/edit/", GameUpdateView.as_view(), name="edit"),
    path("<slug:slug>/delete/", GameDeleteView.as_view(), name="delete"),
    path("<slug:slug>/wishlist/", WishlistView.as_view(), name="wishlist"),
    path("<slug:slug>/played/", PlayedView.as_view(), name="played"),
]