from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views import View

from users.forms import LoginForm, ProfileForm, RegistrationForm
from users.models import UserModel


class PingView(View):
    def get(self, request):
        return render(
            request,
            "users/ping.html",
        )


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        context = {
            "form": form,
        }
        return render(
            request,
            "users/registration.html",
            context=context,
        )

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save()

            new_user.set_password(new_user.password)
            new_user.is_active = True

            new_user.save()

            return redirect("news:all_news")

        context = {
            "form": form,
        }
        return render(
            request,
            "users/registration.html",
            context=context,
        )


class LoginView(View):
    def get(self, request):
        form = LoginForm()

        context = {
            "form": form,
        }

        return render(
            request,
            "users/login.html",
            context=context,
        )

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            email_or_username = form.cleaned_data["email_or_username"]
            password = form.cleaned_data["password"]
            query_find_user = Q(username=email_or_username) | Q(email=email_or_username)  # noqa: E501
            user = UserModel.objects.filter(query_find_user).first()

            if user is None:
                form.add_error(None, "Неверные данные для входа")
                return render(
                    request,
                    "users/login.html",
                    context={"form": form},
                )

            if check_password(password, user.password):
                user.is_active = True
                login(request, user)
                return redirect(
                    "news:all_news",
                )

            form.add_error(None, "Неверные данные для входа")

        context = {
            "form": form,
        }
        return render(
            request,
            "users/login.html",
            context=context,
        )


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(
            "users:login",
        )


class NotLoginedView(View):
    def get(self, request):
        return render(
            request,
            "users/not_logined.html",
        )


class ProfileView(View):
    def get(self, request):
        form = ProfileForm(instance=request.user)
        context = {
            "form": form,
        }
        return render(
            request,
            "users/profile.html",
            context=context,
        )

    def post(self, request):
        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            user = form.save()
            user.save()

            return redirect("users:profile")

        context = {
            "form": form,
        }
        return render(
            request,
            "users/profile.html",
            context=context,
        )
