from typing import Any

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AbstractBaseUser, auth
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request) -> HttpResponse:
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username: Any = request.POST["username"]
            password: Any = request.POST["password"]
            user: AbstractBaseUser | None = auth.authenticate(
                username=username, password=password
            )
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")

                if request.POST.get("next", None):
                    return HttpResponseRedirect(request.POST.get("next"))

                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context: dict[str, str | UserLoginForm] = {
        "title": "Home - Авторизация",
        "form": form,
    }
    return render(request, "users/login.html", context)


def registration(request) -> HttpResponse:
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user: Any = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Вы вошли в аккаунт")
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context: dict[str, str | UserRegistrationForm] = {
        "title": "Home - Регистрация",
        "form": form,
    }
    return render(request, "users/registration.html", context)


@login_required
def profile(request) -> HttpResponse:
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Профаил успешно обновлен")
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance=request.user)

    context: dict[str, str | ProfileForm] = {
        "title": "Home - Кабинет",
        "form": form,
    }
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse("main:index"))
