from django.contrib.auth import login
from django.shortcuts import redirect

from users.models import UserModel


def redirect_with_steam_id(strategy, uid=None, *args, **kwargs):  # noqa: ARG001
    """
    Здесь uid — это SteamID64.
    Мы просто редиректим куда нужно, без регистрации.
    """
    steam_id = uid

    user = UserModel.objects.filter(steamid64=steam_id).first()

    if user:
        user.backend = "django.contrib.auth.backends.ModelBackend"
        login(strategy.request, user)
        return redirect("news:general_news")

    return redirect(
        "users:auth_steam_complete",
        steam_id=steam_id,
    )
