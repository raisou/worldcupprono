from rest_framework import permissions


class MatchPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return True


class TeamPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return True


class PronoPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return True
