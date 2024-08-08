from django.urls import path, include

from . import views


urlpatterns = [
    path("create/", views.ServerCreateView.as_view(), name="create"),
    path("<int:server_id>/", views.ServerDetailView.as_view(), name="detail"),
    path("<int:server_id>/channels/", include(("strife.apps.channels.urls", "channels"), namespace="channels")),
]
