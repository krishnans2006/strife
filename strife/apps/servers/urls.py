from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.ServerCreateView.as_view(), name="create"),
]
