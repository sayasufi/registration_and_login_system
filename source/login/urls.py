from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("register/done", views.register_done, name="register_done"),
    path("profile/", views.ProfileUser.as_view(), name="profile"),
]
