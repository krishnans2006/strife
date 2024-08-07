from django.urls import path, include

from . import views


urlpatterns = [
    path("create/", views.ServerCreateView.as_view(), name="create"),
    path("<int:pk>/", views.ServerDetailView.as_view(), name="detail"),
    path("<int:pk>/channels/", include(("strife.apps.channels.urls", "channels"), namespace="channels")),
]
