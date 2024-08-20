from django.urls import path

from . import views

urlpatterns = [
    path(
        "<int:message_id>/edit/",
        views.message_edit_view,
        name="edit_message",
    ),
    # Must be changed in static/js/websockets/send-handlers/messages.js
    path(
        "<int:message_id>/attachments/upload/",
        views.upload_attachment_view,
        name="upload_attachment",
    ),
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
