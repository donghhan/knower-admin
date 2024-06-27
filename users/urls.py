from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path(
        "search/",
        views.UserSearchView.as_view(
            extra_context={
                "title": "User Search",
                "url_resolver": "users:user_search",
            }
        ),
        name="user_search",
    ),
    path(
        "<int:pk>/update/",
        views.UserProfileUpdateView.as_view(extra_context={"title": "Update User"}),
        name="user_update",
    ),
    path(
        "",
        views.UserListView.as_view(
            extra_context={
                "title": "All Users",
                "url_resolver": "users:user_search",
            }
        ),
        name="user_list",
    ),
]
