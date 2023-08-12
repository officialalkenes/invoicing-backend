from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from .models import (
    Invoice,
    Item,
    InvoiceItem,
    Recurring,
    Project,
    ProjectTask,
    Quote,
)

from .serializers import (
    InvoiceSerializer,
    ItemSerializer,
    InvoiceItemSerializer,
    RecurringSerializer,
    ProjectSerializer,
    ProjectTaskSerializer,
    QuoteSerializer,
)
from .permissions import IsOwnerOrReadOnly  # Import the custom permission


class InvoiceListCreateView(generics.ListCreateAPIView):
    """
    List all invoices or create a new invoice.
    """

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=["Invoices"])
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class InvoiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete an invoice instance.
    """

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ItemListCreateView(generics.ListCreateAPIView):
    """
    List all items or create a new item.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]


class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete an item instance.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]


# Create similar views for other models


class QuoteListCreateView(generics.ListCreateAPIView):
    """
    List all quotes or create a new quote.
    """

    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticated]


class QuoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a quote instance.
    """

    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class RecurringListCreateView(generics.ListCreateAPIView):
    """
    List all recurring invoices or create a new recurring invoice.
    """

    queryset = Recurring.objects.all()
    serializer_class = RecurringSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=["Recurring Invoices"])
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecurringRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a recurring invoice instance.
    """

    queryset = Recurring.objects.all()
    serializer_class = RecurringSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ProjectListCreateView(generics.ListCreateAPIView):
    """
    List all projects or create a new project.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=["Projects"])
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a project instance.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ProjectTaskListCreateView(generics.ListCreateAPIView):
    """
    List all project tasks or create a new project task.
    """

    queryset = ProjectTask.objects.all()
    serializer_class = ProjectTaskSerializer
    permission_classes = [IsAuthenticated]


class ProjectTaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a project task instance.
    """

    queryset = ProjectTask.objects.all()
    serializer_class = ProjectTaskSerializer
    permission_classes = [IsAuthenticated]
