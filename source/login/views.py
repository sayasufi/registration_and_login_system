from django.views.generic import ListView


class Home(ListView):
    template_name = "login/index.html"
    context_object_name = "posts"
    title_page = "Главная страница"

    def get_queryset(self):
        return None
