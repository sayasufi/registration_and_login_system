from django.contrib.auth.views import PasswordChangeDoneView
from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("register/done", views.register_done, name="register_done"),
    path("profile/", views.ProfileUser.as_view(), name="profile"),
    path(
        "password-change/",
        views.UserPasswordChange.as_view(),
        name="password_change",
    ),
    path(
        "password-change/done/",
        PasswordChangeDoneView.as_view(
            template_name="login/password_change_done.html"
        ),
        name="password_change_done",
    ),
]
