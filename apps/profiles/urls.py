from django.urls import path

from .views import (
    UserProfileListCreateView,
    UserProfileDetailView,
    OrganizationProfileCreateView,
)

app_name = "profiles"

urlpatterns = [
    path(
        "user-profiles/", UserProfileListCreateView.as_view(), name="user-profile-list"
    ),
    path(
        "user-profiles/<int:pk>/",
        UserProfileDetailView.as_view(),
        name="user-profile-detail",
    ),
    path(
        "organization-profiles/",
        OrganizationProfileCreateView.as_view(),
        name="organization-profile-create",
    ),
]
