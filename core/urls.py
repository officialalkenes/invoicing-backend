from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/v1/", include("apps.user.urls", namespace="accounts")),
    path("api/v1/records", include("apps.records.urls", namespace="records")),
    path("admin/", admin.site.urls),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair_view"),
    path(
        "api/v1/token/refresh",
        TokenRefreshView.as_view(),
        name="token_obtain_refresh_view",
    ),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.authtoken")),
]
