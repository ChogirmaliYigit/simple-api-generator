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
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CategoryDetailView(BaseAPIView):
    model = Category
    serializer_class = CategorySerializer

    def get_category(self, request, pk):
        return get_object_or_404(self.model, pk=pk, app=request.app)

    def put(self, request, pk):
        category = self.get_category(request, pk)
        serializer = self.serializer_class(
            instance=category, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk):
        category = self.get_category(request, pk)
        category.deleted_at = timezone.now()
        category.save()
        return Response({}, status.HTTP_204_NO_CONTENT)
