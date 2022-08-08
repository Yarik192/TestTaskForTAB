from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def homepage(request: HttpRequest) -> HttpResponse:
    """
    Главная страница с которой осуществляется переход на страницу входа в аккаунт.
    :return HttpResponse:
    """
    return render(request, "index.html")
