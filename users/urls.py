from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path(
        "<int:pk>/update/",
        views.UserProfileUpdateView.as_view(extra_context={"title": "Update User"}),
        name="user_update",
    ),
    path(
        "",
        views.UserListView.as_view(extra_context={"title": "All Users"}),
        name="user_list",
    ),
]
