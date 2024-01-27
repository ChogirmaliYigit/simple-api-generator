from rest_framework import permissions


class HasApplicationPermission(permissions.BasePermission):
    message = "You do not have permission to access this application."

    def has_permission(self, request, view):
        if hasattr(request, "app") and request.app:
            return request.user.is_authenticated and request.app.owner == request.user
        return False
