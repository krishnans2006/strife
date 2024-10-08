from django.urls import include, path

from . import views

urlpatterns = [
    path("create/text/", views.TextChannelCreateView.as_view(), name="create_text"),
    path("<int:channel_id>/", views.TextChannelDetailView.as_view(), name="detail"),
    path(
        "<int:channel_id>/messages/",
        include(("strife.apps.messages.urls", "messages"), namespace="messages"),
    ),
]
