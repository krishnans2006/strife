from django.http import HttpResponseNotAllowed

from .models import Message


def send_message_view(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    content = request.POST.get("content")
    channel_id = request.POST.get("channel_id")

    if not content or not channel_id:
        return {"result": False, "error": "Missing content or channel_id"}

    Message.objects.create(
        author=request.user,
        channel_id=channel_id,
        content=content
    )

    return {"result": True}
