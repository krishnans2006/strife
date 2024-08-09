import json

from django.http import HttpResponseNotAllowed, JsonResponse

from .models import Message


def send_message_view(request, _server_id, channel_id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    content = json.loads(request.body).get("content")
    print(content)

    if not content:
        return JsonResponse({"result": False, "error": "Missing content"})

    Message.objects.create(
        author=request.user,
        channel_id=channel_id,
        content=content
    )

    return JsonResponse({"result": True})
