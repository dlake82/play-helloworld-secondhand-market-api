from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets.views import SnippetViewSet
from users.views import UserViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"", SnippetViewSet, basename="snippet")
router.register(r"users", UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
