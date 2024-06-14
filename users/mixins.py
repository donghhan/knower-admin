from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect


class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self) -> bool | None:
        return not self.request.user.is_authenticated

    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.error(self.request, "You should be logged out")
        return redirect("common:home")
