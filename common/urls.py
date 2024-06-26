from django.urls import path
from . import views

app_name = "common"

urlpatterns = [
    path(
        "login/",
        views.LoginView.as_view(extra_context={"title": "Login"}),
        name="login",
    ),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("", views.HomeView.as_view(extra_context={"title": "Home"}), name="home"),
]
