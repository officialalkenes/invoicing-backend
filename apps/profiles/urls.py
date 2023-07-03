from django.urls import path

from . import api_views

urlpatterns = [path("", api_views.update_user_profiles, name="update-profiles")]
