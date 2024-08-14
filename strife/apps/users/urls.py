from django.urls import path

from . import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("profile/edit/", views.EditView.as_view(), name="edit"),
    path("logout/", views.logout_view, name="logout"),
]
