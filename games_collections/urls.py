from django.urls import path
from .views import CollectionListView, CollectionDetailView, CollectionCreateView, CollectionUpdateView, \
    CollectionDeleteView

app_name = "collections"

urlpatterns = [
    path("", CollectionListView.as_view(), name="list"),
    path("create/", CollectionCreateView.as_view(), name="create"),
    path("<slug:slug>/", CollectionDetailView.as_view(), name="detail"),
    path("<slug:slug>/edit/", CollectionUpdateView.as_view(), name="edit"),
    path("<slug:slug>/delete/", CollectionDeleteView.as_view(), name="delete"),
]