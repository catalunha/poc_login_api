from rest_framework import permissions


class IsQwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # return obj.id == request.user
        # print(request.method)
        # print('has_object_permission')
        # if request.method is
        # return False
        return super().has_object_permission(request, view, obj)

    def has_permission(self, request, view):
        print('has_permission')
        # print(request.method)
        if request.method == 'POST':
            print('permitido')
            return True
        return super().has_permission(request, view)
