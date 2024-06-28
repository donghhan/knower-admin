from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path(
        "search/",
        views.ProductSearchView.as_view(
            extra_context={
                "title": "Search Product",
                "search_view_url_resolver": "products:product_search",
            }
        ),
        name="product_search",
    ),
    path(
        "<int:pk>/",
        views.ProductUpdateView.as_view(
            extra_context={
                "title": "Update Product",
            }
        ),
        name="product_update",
    ),
    path(
        "",
        views.ProductListView.as_view(
            extra_context={
                "title": "All Products",
                "search_view_url_resolver": "products:product_search",
            }
        ),
        name="product_list",
    ),
]
