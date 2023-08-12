from django.urls import path
from . import views

app_name = "invoices"

urlpatterns = [
    path(
        "invoices/", views.InvoiceListCreateView.as_view(), name="invoice-list-create"
    ),
    path(
        "invoices/<int:pk>/",
        views.InvoiceRetrieveUpdateDestroyView.as_view(),
        name="invoice-retrieve-update-destroy",
    ),
    path("items/", views.ItemListCreateView.as_view(), name="item-list-create"),
    path(
        "items/<int:pk>/",
        views.ItemRetrieveUpdateDestroyView.as_view(),
        name="item-retrieve-update-destroy",
    ),
    path(
        "recurring/",
        views.RecurringListCreateView.as_view(),
        name="recurring-list-create",
    ),
    path(
        "recurring/<int:pk>/",
        views.RecurringRetrieveUpdateDestroyView.as_view(),
        name="recurring-retrieve-update-destroy",
    ),
    path(
        "projects/", views.ProjectListCreateView.as_view(), name="project-list-create"
    ),
    path(
        "projects/<int:pk>/",
        views.ProjectRetrieveUpdateDestroyView.as_view(),
        name="project-retrieve-update-destroy",
    ),
    path(
        "project-tasks/",
        views.ProjectTaskListCreateView.as_view(),
        name="project-task-list-create",
    ),
    path(
        "project-tasks/<int:pk>/",
        views.ProjectTaskRetrieveUpdateDestroyView.as_view(),
        name="project-task-retrieve-update-destroy",
    ),
    path("quotes/", views.QuoteListCreateView.as_view(), name="quote-list-create"),
    path(
        "quotes/<int:pk>/",
        views.QuoteRetrieveUpdateDestroyView.as_view(),
        name="quote-retrieve-update-destroy",
    ),
]
