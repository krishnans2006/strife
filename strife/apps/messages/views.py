from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.files.images import ImageFile
from django.http import FileResponse, HttpResponse, HttpResponseForbidden

from .models import Attachment, Message


def upload_attachment_view(request, server_id, channel_id, message_id):
    if not request.user.as_serverized(server_id).can_send_attachments:
        return HttpResponseForbidden()

    message = Message.objects.get(id=message_id)

    if (
        message.author != request.user
        or message.channel.id != channel_id
        or message.channel.server.id != server_id
    ):
        return HttpResponseForbidden()

    file_obj = request.FILES["file"]
    file = ImageFile(file_obj)
    filename = file.name

    message.attachments.create(
        filename=filename,
        file=file,
    )

    channel_layer = get_channel_layer()
    group_name = f"chat_{channel_id}"
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            "type": "chat.attachment",
            "message": message.to_dict(),
        },
    )

    # The server successfully processed the request, and is not returning any content
    return HttpResponse(status=204)


def view_attachment_view(request, server_id, channel_id, message_id, attachment_id):
    attachment = Attachment.objects.get(id=attachment_id)

    file_obj = open(attachment.file.path, "rb")

    return FileResponse(file_obj, filename=attachment.filename, as_attachment=False)


def download_attachment_view(request, server_id, channel_id, message_id, attachment_id):
    attachment = Attachment.objects.get(id=attachment_id)

    file_obj = open(attachment.file.path, "rb")

    return FileResponse(file_obj, filename=attachment.filename, as_attachment=True)
