from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import permissions, views
from rest_framework.generics import CreateAPIView

from .serializers import RegisterUserSerializer


User = get_user_model()
