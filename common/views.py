from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, views
from django.views import generic
from users.mixins import LoggedOutOnlyView
from users.models import User
from users.forms import LoginForm


def home(request):
    return render(request, "home.html")


class LoginView(views.LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    authentication_form = LoginForm
    success_url = reverse_lazy("common:home")


class LogoutView(views.LogoutView):
    next_page = reverse_lazy("common:login")
