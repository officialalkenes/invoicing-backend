from rest_framework import status, permissions, views

from .models import UserProfile, OrganizationProfile
from .serializers import ProfileSerializers, OrganizationProfileSerializer


class UpdateUserProfiles(views.APIView):
    serializer_class = ProfileSerializers
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def update(self, user):
        return super().save()


update_user_profile = UpdateUserProfiles.as_view()


class UpdateOrganizationProfiles(views.APIView):
    serializer_class = OrganizationProfile
    queryset = OrganizationProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def update(self, user):
        return super().save()
