from django.urls import path
from shop.views.category import CategoryDetailView, CategoryListView
from shop.views.product import ProductDetailView, ProductListView

urlpatterns = [
    path("category", CategoryListView.as_view(), name="categories-list"),
    path("category/<int:pk>", CategoryDetailView.as_view(), name="category-detail"),
    path("product", ProductListView.as_view(), name="products-list"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product-detail"),
]
