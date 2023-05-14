from rest_framework import permissions
from krBackend.models import *


class IsAuthorUpdate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method is permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.method == 'GET':
            return bool(request.user and request.user.is_authenticated)
        else:
            return bool(request.user.is_authenticated and User.objects.filter(pk=request.user.id, groups__name='Author').exists())


class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_authenticated)


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method is permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)
