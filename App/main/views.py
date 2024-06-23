from django.http import HttpResponse
from django.shortcuts import render 
# Create your views here.

def index(request) -> HttpResponse:
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, "main/index.html", context)

def about(request) -> HttpResponse:
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Текс о том почему этот магазин такой классный и какой хороший товар",
    }
    return render(request, "main/about.html", context)

