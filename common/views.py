from django.shortcuts import render
from django.views.generic import View, DetailView, ListView, UpdateView


def home(request):
    return render(request, "home.html")
