from django.http import FileResponse

from .models import Attachment


def view_attachment_view(request, server_id, channel_id, message_id, attachment_id):
    attachment = Attachment.objects.get(id=attachment_id)

    file_obj = open(attachment.file.path, "rb")

    return FileResponse(file_obj, filename=attachment.filename, as_attachment=False)


def download_attachment_view(request, server_id, channel_id, message_id, attachment_id):
    attachment = Attachment.objects.get(id=attachment_id)

    file_obj = open(attachment.file.path, "rb")

    return FileResponse(file_obj, filename=attachment.filename, as_attachment=True)
