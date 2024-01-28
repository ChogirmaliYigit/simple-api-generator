from applications.models import Application
from applications.serializers.apps import AppsListSerializer
from core.views.base import BaseAPIView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import response, status, views


class AppsListView(views.APIView):
    def get(self, request):
        queryset = Application.objects.filter(owner=request.user)
        serializer = AppsListSerializer(queryset, many=True)
        return response.Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = AppsListSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status.HTTP_201_CREATED)


class AppDetailView(BaseAPIView):
    def put(self, request, pk):
        category = get_object_or_404(Application, pk=pk, app=request.app)
        serializer = AppsListSerializer(
            instance=category, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk):
        category = get_object_or_404(Application, pk=pk, app=request.app)
        category.deleted_at = timezone.now()
        category.save()
        return response.Response({}, status.HTTP_204_NO_CONTENT)
