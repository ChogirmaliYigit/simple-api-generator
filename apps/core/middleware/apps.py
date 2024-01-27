import uuid
from django.shortcuts import get_object_or_404
from applications.models import Application


class ApplicationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            request.app = get_object_or_404(Application, uuid=uuid.UUID(request.headers.get("AppToken")))
        except Exception as e:
            request.app = None

        response = self.get_response(request)
        return response
