from typing import Any
from django.contrib.auth.models import AbstractBaseUser, auth
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm


def login(request) -> HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username: Any = request.POST["username"]
            password: Any = request.POST["password"]
            user: AbstractBaseUser | None = auth.authenticate(
                username=username, password=password
            )
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context: dict[str, str] = {
        "title": "Home - Авторизация",
        "form": form,
    }
    return render(request, "users/login.html", context)


def registration(request) -> HttpResponse:
    context: dict[str, str] = {"title": "Home - Регистрация"}
    return render(request, "users/registration.html", context)


def profile(request) -> HttpResponse:
    context: dict[str, str] = {"title": "Home - Кабинет"}
    return render(request, "users/profile.html", context)


def logout(request): ...
