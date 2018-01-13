from rest_framework import permissions

from .models import Match


class PronoPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            try:
                return not Match.objects.get(
                    pk=request.data.get('match')).is_locked
            except:
                return False

        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated() and not obj.match.is_locked:
            return True
        return False
