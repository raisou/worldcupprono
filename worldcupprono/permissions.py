from rest_framework import permissions


class GlobalUserPermission(permissions.BasePermission):
    """
    Base permission
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated()
