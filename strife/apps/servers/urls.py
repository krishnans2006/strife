from django.urls import include, path

from . import views

urlpatterns = [
    path("create/", views.ServerCreateView.as_view(), name="create"),
    path("<int:server_id>/", views.ServerDetailView.as_view(), name="detail"),
    path("<int:server_id>/edit/", views.ServerEditView.as_view(), name="edit"),
    path(
        "<int:server_id>/channels/",
        include(("strife.apps.channels.urls", "channels"), namespace="channels"),
    ),
    path(
        "<int:server_id>/roles/", include(("strife.apps.roles.urls", "roles"), namespace="roles")
    ),
]
