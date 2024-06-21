from django.db.models import Q
from django.views import generic
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from . import models, forms


class UserListView(generic.ListView):
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


class UserSearchView(generic.ListView):
    model = models.User

    def get_queryset(self):
        user_search_keyword = self.kwargs.get("user_search_keyword")
        if user_search_keyword:
            queryset = models.User.objects.get(
                Q(email__icontains=user_search_keyword)
                | Q(first_name__icontains=user_search_keyword)
                | Q(last_name__icontains=user_search_keyword)
            )
        else:
            queryset = models.User.objects.none()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(UserSearchView, self).get_context_data(*args, **kwargs)
        context["searched_user"] = self.get_queryset()
        return context


class UserProfileUpdateView(UpdateView):
    context_object_name = "user"
    template_name = "users/user_detail.html"
    model = models.User
    success_url = reverse_lazy("users:user_list")
    fields = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "is_active",
        "is_staff",
    ]

    def form_valid(self, form):
        messages.success(self.request, "Profile updated successfully.")
        return super().form_valid(form)

    # fields = [
    #     "first_name",
    #     "last_name",
    #     "email",
    #     "phone_number",
    #     "is_active",
    #     "is_staff",
    # ]

    # def get_success_url(self):
    #     return reverse_lazy("users:user_list")
