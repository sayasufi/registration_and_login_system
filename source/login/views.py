from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from login.forms import LoginUserForm, RegisterUserForm


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


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
