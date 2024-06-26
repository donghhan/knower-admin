from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("common.urls")),
    path("products/", include("products.urls")),
    path("users/", include("users.urls")),
    path("admin/", admin.site.urls),
]
