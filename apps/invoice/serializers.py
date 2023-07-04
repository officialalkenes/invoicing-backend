from rest_framework import serializers
from .models import Invoice, Project, ProjectTask, Quote


class ProjectTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTask
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    tasks = ProjectTaskSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class QuoteSerializer(serializers.ModelSerializer):
    project_name = ProjectSerializer()

    class Meta:
        model = Quote
        fields = "__all__"


class ProjectTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTask
        fields = "__all__"


class ProjectCreateSerializer(serializers.ModelSerializer):
    tasks = ProjectTaskCreateSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"

    def create(self, validated_data):
        tasks_data = validated_data.pop("tasks", [])
        project = Project.objects.create(**validated_data)
        for task_data in tasks_data:
            project.tasks.add(ProjectTask.objects.create(**task_data))
        return project


class QuoteCreateSerializer(serializers.ModelSerializer):
    project_name = ProjectCreateSerializer()

    class Meta:
        model = Quote
        fields = "__all__"

    def create(self, validated_data):
        project_data = validated_data.pop("project_name", {})
        tasks_data = project_data.pop("tasks", [])
        project = Project.objects.create(**project_data)
        for task_data in tasks_data:
            project.tasks.add(ProjectTask.objects.create(**task_data))
        validated_data["project_name"] = project
        return super().create(validated_data)


class InvoiceSerializer(serializers.Modelserializer):
    class Meta:
        model = Invoice
        fields = "__all__"

    def create(self, validated_data):
        ...
