# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.views import APIView


class RegistrationView(APIView):
    """
    Регистрация пользователей через Telegram бота, по средствам POST запроса.
    """
    def post(self, request, *args, **kwargs):
        username = request.POST["login"]
        passwd = request.POST["password"]
        User.objects.create_user(username=username, password=passwd)
        return HttpResponse(status=201)
