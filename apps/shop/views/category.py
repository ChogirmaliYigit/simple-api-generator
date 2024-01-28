from core.views.base import BaseAPIView, BaseListAPIView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from shop.models import Category
from shop.serializers.category import CategorySerializer


class CategoryListView(BaseListAPIView):
    serializer_class = CategorySerializer
    search_fields = ["title", "description"]

    def get_queryset(self):
        return Category.objects.filter(app=self.request.app)

    def post(self, request):
        serializer = CategorySerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CategoryDetailView(BaseAPIView):
    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk, app=request.app)
        serializer = CategorySerializer(
            instance=category, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk, app=request.app)
        category.deleted_at = timezone.now()
        category.save()
        return Response({}, status.HTTP_204_NO_CONTENT)
