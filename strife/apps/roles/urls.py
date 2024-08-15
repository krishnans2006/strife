from django.urls import path, include

from . import views


urlpatterns = [
    path("create/", views.RoleCreateView.as_view(), name="create"),
    path("<int:role_id>/edit/", views.RoleEditView.as_view(), name="edit"),
]
