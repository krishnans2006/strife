import json

from django.http import HttpResponseNotAllowed, JsonResponse, FileResponse

from .models import Message, Attachment


def send_message_view(request, server_id, channel_id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    content = json.loads(request.body).get("content")

    if not content:
        return JsonResponse({"result": False, "error": "Missing content"})

    Message.objects.create(
        author=request.user,
        channel_id=channel_id,
        content=content
    )

    return JsonResponse({"result": True})


def view_attachment_view(request, server_id, channel_id, message_id, attachment_id):
    attachment = Attachment.objects.get(id=attachment_id)

    file_obj = open(attachment.file.path, "rb")

    return FileResponse(file_obj, filename=attachment.filename, as_attachment=False)


def download_attachment_view(request, server_id, channel_id, message_id, attachment_id):
    attachment = Attachment.objects.get(id=attachment_id)

    file_obj = open(attachment.file.path, "rb")

    return FileResponse(file_obj, filename=attachment.filename, as_attachment=True)
