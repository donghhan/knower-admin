from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from . import models


class UserListView(ListView):
    model = models.User
    paginate_by = 20
    paginate_orphans = 5
    context_object_name = "users"


class UserSearchView(ListView):
    model = models.User
    template_name = "users/user_search.html"
    paginate_by = 20
    paginate_orphans = 5
    context_object_name = "searched_users"

    def get_queryset(self):
        search_keyword = self.request.GET.get("search_keyword")
        object_list = models.User.objects.filter(
            Q(email__icontains=search_keyword)
            | Q(first_name__icontains=search_keyword)
            | Q(last_name__icontains=search_keyword)
        )
        return object_list


class UserProfileUpdateView(UpdateView):
    model = models.User
    template_name = "users/user_update.html"
    fields = [
        "first_name",
        "last_name",
        "phone_number",
        "is_active",
        "is_admin",
    ]
    success_url = reverse_lazy("users:user_list")
