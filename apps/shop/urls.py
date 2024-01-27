from django.urls import path
from shop.views.category import CategoryListView, CategoryDetailView
from shop.views.product import ProductListView, ProductDetailView


urlpatterns = [
    path("category", CategoryListView.as_view(), name="categories-list"),
    path("category/<int:pk>", CategoryDetailView.as_view(), name="category-detail"),
    path("product", ProductListView.as_view(), name="products-list"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product-detail"),
]
