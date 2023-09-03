from rest_framework import permissions


class IsQwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user
      # return super().has_object_permission(request, view, obj)

    def has_permission(self, request, view):
        return super().has_permission(request, view)
