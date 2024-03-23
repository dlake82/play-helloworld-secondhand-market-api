from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework import routers
from users.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    # Add Log in Button in rest_framework page
    path("api-auth/", include("rest_framework.urls")),
    # simple-jwt
    path("account/", include("account.urls")),
    path("snippets/", include("snippets.urls")),
]

urlpatterns += router.urls
