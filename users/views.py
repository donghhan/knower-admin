from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from . import models


class UserListView(ListView):
    model = models.User
    paginate_by = 20
    paginate_orphans = 5
    ordering = "created_at"
    context_object_name = "users"

    def get_context_data(self, *args, **kwargs):
        context = super(UserListView, self).get_context_data(*args, **kwargs)
        context["all_users"] = models.User.objects.all()
        return context

    def get_queryset(self):
        return models.User.objects.all()

    def paginate_queryset(self, queryset, page_size):
        return super().paginate_queryset(queryset, page_size)


class UserSearchView(ListView):
    model = models.User
    template_name = "users/user_search.html"

    def get_queryset(self):
        search_keyword = self.request.GET.get("search_keyword")
        object_list = models.User.objects.filter(
            Q(email__icontains=search_keyword)
            | Q(first_name__icontains=search_keyword)
            | Q(last_name__icontains=search_keyword)
        )
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super(UserSearchView, self).get_context_data(*args, **kwargs)
        context["searched_users"] = self.get_queryset()
        return context


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
