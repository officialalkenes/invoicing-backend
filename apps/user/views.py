from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from .serializers import RegisterUserSerializer


User = get_user_model()


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterUserSerializer


register = RegisterUserView.as_view()
