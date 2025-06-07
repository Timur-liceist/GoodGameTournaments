from django.urls import path

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
        "profile",
        ProfileView.as_view(),
        name="profile",
    ),
]
