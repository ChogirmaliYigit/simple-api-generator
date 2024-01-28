from core.views.base import BaseAPIView, BaseListAPIView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from shop.filters.product import ProductFilterBackend
from shop.models import Product
from shop.serializers.product import ProductSerializer


class ProductListView(BaseListAPIView):
    serializer_class = ProductSerializer
    search_fields = ["title", "description"]
    filter_backends = [ProductFilterBackend]

    def get_queryset(self):
        return Product.objects.filter(app=self.request.app)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class ProductDetailView(BaseAPIView):
    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk, app=request.app)
        serializer = ProductSerializer(
            instance=product, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk, app=request.app)
        product.deleted_at = timezone.now()
        product.save()
        return Response({}, status.HTTP_204_NO_CONTENT)
