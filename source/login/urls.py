from django.contrib.auth.views import (
    LogoutView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import path, reverse_lazy

from . import views

app_name = "login"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
]