from core.permission.application import HasApplicationPermission
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView


class BaseView:
    permission_classes = (HasApplicationPermission,)
    filter_backends = [SearchFilter]


class BaseAPIView(BaseView, APIView):
    pass


class BaseListAPIView(BaseView, ListAPIView):
    pass
