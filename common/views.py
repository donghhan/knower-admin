from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views import generic
from users.mixins import LoggedOutOnlyView
from users.models import User
from users.forms import LoginForm


class HomeView(generic.TemplateView):
    template_name = "common/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_users"] = User.objects.all().count()
        return context


class LoginView(auth_views.LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True
    authentication_form = LoginForm
    success_url = reverse_lazy("common:home")


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy("common:login")
