from rest_framework.permissions import BasePermission

class IsAdminPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(111)
        if obj.user.is_superuser:
            return True
        else:
            return False