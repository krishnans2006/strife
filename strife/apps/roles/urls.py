from django.urls import path

from . import views

urlpatterns = [
    path("", views.RoleIndexView.as_view(), name="index"),
    path("create/", views.RoleCreateView.as_view(), name="create"),
    path("<int:role_id>/edit/", views.role_edit_view, name="edit"),
    path("<int:role_id>/delete/", views.RoleDeleteView.as_view(), name="delete"),
]
