from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.ChannelCreateView.as_view(), name="create"),
]
