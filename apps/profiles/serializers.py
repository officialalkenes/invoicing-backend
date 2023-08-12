# serializers.py
from rest_framework import serializers
from .models import UserProfile, OrganizationProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        read_only_fields = ("user",)

    def create(self, validated_data):
        # Automatically set the user field to the authenticated user
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Automatically update the user field to the authenticated user
        validated_data["user"] = self.context["request"].user
        return super().update(instance, validated_data)


class OrganizationProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationProfile
        fields = "__all__"

    def create(self, validated_data):
        # Automatically set the organization field to the authenticated user's profile
        validated_data["organization"] = self.context["request"].user.user_profile
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Automatically update the organization field to the authenticated user's profile
        validated_data["organization"] = self.context["request"].user.user_profile
        return super().update(instance, validated_data)
