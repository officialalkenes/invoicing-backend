from rest_framework import serializers
from .models import (
    Invoice,
    Item,
    InvoiceItem,
    Recurring,
    Project,
    ProjectTask,
    Quote,
)


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = "__all__"


class InvoiceSerializer(serializers.ModelSerializer):
    invoice_items = InvoiceItemSerializer(many=True, required=False)

    class Meta:
        model = Invoice
        fields = "__all__"
        read_only_fields = ("user",)

    def create(self, validated_data):
        user = self.context["request"].user
        invoice_items_data = validated_data.pop("invoice_items", [])
        invoice = Invoice.objects.create(user=user, **validated_data)
        for item_data in invoice_items_data:
            InvoiceItem.objects.create(invoice=invoice, **item_data)
        return invoice


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class RecurringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurring
        fields = "__all__"
        read_only_fields = ("user",)


class ProjectTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTask
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    tasks = ProjectTaskSerializer(many=True, required=False)

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ("user",)

    def create(self, validated_data):
        user = self.context["request"].user
        tasks_data = validated_data.pop("tasks", [])
        project = Project.objects.create(user=user, **validated_data)
        for task_data in tasks_data:
            ProjectTask.objects.create(project=project, **task_data)
        return project


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = "__all__"
        read_only_fields = ("user",)
