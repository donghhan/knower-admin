from django.urls import path
from . import views

app_name = "common"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("", views.home, name="home"),
]
