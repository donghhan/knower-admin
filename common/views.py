from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from users.models import User
from users.forms import LoginForm


def home(request):
    return render(request, "home.html")


class LoginView(generic.FormView):
    model = User
    form_class = LoginForm
    template_name = "login.html"

    def form_valid(self, form) -> HttpResponse:
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        authenticate_user = authenticate(self.request, email=email, password=password)

        if authenticate_user is not None:
            login(self.request, authenticate_user)

        return super().form_valid(form)

    def get_success_url(self) -> str:
        next_arg = self.request.GET.get("next")
        return next_arg if next_arg is not None else reverse("common:home")
