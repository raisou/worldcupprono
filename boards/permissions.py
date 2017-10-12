from rest_framework import permissions


class BoardPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # Owner can do anything, don't go any further
        if request.user in obj.users.all():
            return True
