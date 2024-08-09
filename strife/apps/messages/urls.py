from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.send_message_view, name="create"),
]
