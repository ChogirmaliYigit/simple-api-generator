from core.permission.application import HasApplicationPermission
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from shop.models import Product
from shop.serializers.product import ProductSerializer


class ProductListView(APIView):
    permission_classes = (HasApplicationPermission,)

    def get(self, request):
        if hasattr(request, "app") and request.app:
            products = Product.objects.filter(app=request.app)
        else:
            products = []
        return Response(
            ProductSerializer(instance=products, many=True).data, status.HTTP_200_OK
        )

    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class ProductDetailView(APIView):
    permission_classes = (HasApplicationPermission,)

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
