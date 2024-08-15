from django.urls import path, include

from . import views


urlpatterns = [
    path("create/", views.RoleCreateView.as_view(), name="create"),
    path("list/", views.RoleListView.as_view(), name="list"),
    path("<int:role_id>/edit/", views.RoleEditView.as_view(), name="edit"),
    path("<int:role_id>/delete/", views.RoleDeleteView.as_view(), name="delete"),
]
