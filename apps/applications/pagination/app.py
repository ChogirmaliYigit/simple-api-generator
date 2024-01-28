from django.conf import settings
from django.db.models import ObjectDoesNotExist
from rest_framework.pagination import PageNumberPagination


class AppPagination(PageNumberPagination):
    def get_page_size(self, request):
        page_size = settings.REST_FRAMEWORK["PAGE_SIZE"]
        try:
            if hasattr(request, "app") and request.app:
                page_size = request.app.config.page_size
        except ObjectDoesNotExist:
            pass
        return page_size
