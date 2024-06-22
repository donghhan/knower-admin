from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path(
        "<int:pk>/",
        views.ProductUpdateView.as_view(extra_context={"title": "Update Product"}),
        name="product_update",
    ),
    path(
        "",
        views.ProductListView.as_view(extra_context={"title": "All Products"}),
        name="product_list",
    ),
]
