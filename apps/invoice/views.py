from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Project, ProjectTask, Quote
from .serializers import (
    ProjectSerializer,
    ProjectTaskSerializer,
    QuoteSerializer,
    ProjectCreateSerializer,
    QuoteCreateSerializer,
)


class ProjectListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectCreateSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            return Response(ProjectSerializer(project).data, status=201)
        return Response(serializer.errors, status=400)


class ProjectDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        project = generics.get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = generics.get_object_or_404(Project, pk=pk)
        serializer = ProjectCreateSerializer(project, data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            return Response(ProjectSerializer(project).data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        project = generics.get_object_or_404(Project, pk=pk)
        project.delete()
        return Response(status=204)


class ProjectTaskListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = ProjectTask.objects.all()
        serializer = ProjectTaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectTaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            return Response(ProjectTaskSerializer(task).data, status=201)
        return Response(serializer.errors, status=400)


class QuoteListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuoteCreateSerializer(data=request.data)
        if serializer.is_valid():
            quote = serializer.save()
            return Response(QuoteSerializer(quote).data, status=201)
        return Response(serializer.errors, status=400)


class QuoteDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        quote = generics.get_object_or_404(Quote, pk=pk)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)

    def put(self, request, pk):
        quote = generics.get_object_or_404(Quote, pk=pk)
        serializer = QuoteCreateSerializer(quote, data=request.data)
        if serializer.is_valid():
            quote = serializer.save()
            return Response(QuoteSerializer(quote).data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        quote = generics.get_object_or_404(Quote, pk=pk)
        quote.delete()
        return Response(status=204)
