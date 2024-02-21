from applications.models import Application
from applications.serializers.apps import AppsListSerializer
from core.views.base import BaseAPIView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import response, status, views


class AppsListView(views.APIView):
    model = Application
    serializer = AppsListSerializer

    def get(self, request):
        queryset = self.model.objects.filter(owner=request.user)
        serializer = self.serializer(queryset, many=True)
        return response.Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status.HTTP_201_CREATED)


class AppDetailView(BaseAPIView):
    model = Application
    serializer = AppsListSerializer

    def get_application(self, request, pk):
        return get_object_or_404(self.model, pk=pk, app=request.app)

    def put(self, request, pk):
        category = self.get_application(request, pk)
        serializer = self.serializer(instance=category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk):
        category = self.get_application(request, pk)
        category.deleted_at = timezone.now()
        category.save()
        return response.Response({}, status.HTTP_204_NO_CONTENT)
