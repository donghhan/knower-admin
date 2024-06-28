from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 20
    paginate_orphans = 5
    ordering = "pk"
    context_object_name = "products"
    template_name = "products/product_list.html"


class ProductSearchView(ListView):
    model = Product
    paginate_by = 20
    paginate_orphans = 5
    ordering = "pk"
    template_name = "products/product_search.html"
    context_object_name = "searched_products"

    def get_queryset(self):
        search_keyword = self.request.GET.get("search_keyword")
        object_list = Product.objects.filter(name__icontains=search_keyword)
        return object_list


class ProductUpdateView(UpdateView):
    model = Product
    context_object_name = "product"
    template_name = "products/product_update.html"
    fields = [
        "name",
        "price",
        "discount_price",
        "detail",
        "description",
    ]
    success_url = reverse_lazy("products:product_list")
