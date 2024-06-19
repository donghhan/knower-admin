from django.urls import path
from django.urls import resolve
from . import views

app_name = "users"

urlpatterns = [
    path(
        "<str:user_search_keyword>/", views.UserSearchView.as_view(), name="user_search"
    ),
    path(
        "",
        views.UserListView.as_view(extra_context={"title": "All Users"}),
        name="user_list",
    ),
]
