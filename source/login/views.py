from django.conf import settings
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from login.forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm


class Home(ListView):
    template_name = "login/index.html"
    context_object_name = "posts"
    title_page = "Главная страница"
    extra_context = {"title": "Главная страница"}

    def get_queryset(self):
        return None


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "login/login.html"
    extra_context = {"title": "Авторизация"}
    next_page = "/profile"


def logout_view(request):
    logout(request)
    return redirect("home")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "login/register.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("register_done")


def register_done(request):
    return render(request, "login/register_done.html")


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = "login/profile.html"
    extra_context = {'title': "Профиль пользователя", 'default_image': settings.DEFAULT_USER_IMAGE}

    def get_success_url(self):
        return reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("password_change_done")
    template_name = "login/password_change_form.html"
    extra_context = {"title": "Изменение пароля"}


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
