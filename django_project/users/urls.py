from django.urls import path
from django.views.generic import TemplateView

from users.views import (
    LoginView,
    LogoutView,
    PingView,
    ProfileView,
    RegistrationView,
)

app_name = "users"

urlpatterns = [
    path(
        "ping",
        PingView.as_view(),
        name="ping",
    ),
    path(
        "registration",
        RegistrationView.as_view(),
        name="registration",
    ),
    path(
        "login",
        LoginView.as_view(),
        name="login",
    ),
    path(
        "logout",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "<int:user_id>/profile",
        ProfileView.as_view(),
        name="profile",
    ),
    path(
        "not_logined",
        TemplateView.as_view(
            template_name="includes/error.html",
            extra_context={
                "error_message": "Вы не авторизованы",
            },
        ),
        name="not_logined",
    ),
    path(
        "not_public_profile",
        TemplateView.as_view(
            template_name="includes/error.html",
            extra_context={
                "error_message": "Профиль приватный",
            },
        ),
        name="not_public_profile",
    ),
]
