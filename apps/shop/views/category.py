from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils import timezone
from core.permission.application import HasApplicationPermission
from shop.models import Category
from shop.serializers.category import CategorySerializer


class CategoryListView(APIView):
    permission_classes = (HasApplicationPermission, )

    def get(self, request):
        if hasattr(request, "app") and request.app:
            categories = Category.objects.filter(app=request.app)
        else:
            categories = []
        return Response(CategorySerializer(instance=categories, many=True).data, status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CategoryDetailView(APIView):
    permission_classes = (HasApplicationPermission,)

    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk, app=request.app)
        serializer = CategorySerializer(instance=category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk, app=request.app)
        category.deleted_at = timezone.now()
        category.save()
        return Response({}, status.HTTP_204_NO_CONTENT)
