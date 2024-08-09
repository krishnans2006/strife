from django.urls import path

from . import views


urlpatterns = [
    path("create/text/", views.TextChannelCreateView.as_view(), name="create_text"),
]
