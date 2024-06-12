from django.shortcuts import render
from django.views import generic
from . import models


class UserListView(generic.ListView):
    model = models.User
    paginate_by = 20
    paginate_orphans = 5
    ordering = "created_at"
