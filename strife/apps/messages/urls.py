from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.send_message_view, name="create"),
    path(
        "<int:message_id>/attachments/<int:attachment_id>/view/",
        views.view_attachment_view,
        name="view_attachment",
    ),
    path(
        "<int:message_id>/attachments/<int:attachment_id>/download/",
        views.download_attachment_view,
        name="download_attachment",
    ),
]
