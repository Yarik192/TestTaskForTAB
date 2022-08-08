from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from profile_users.views import RegistrationView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register_tg/", RegistrationView.as_view(), name="register_tg")
]
