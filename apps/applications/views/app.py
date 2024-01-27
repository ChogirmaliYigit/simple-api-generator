from applications.models import Application
from applications.serializers.apps import AppsListSerializer
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
