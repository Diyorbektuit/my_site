from rest_framework.permissions import BasePermission

class IsAdminPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        print("permission")
        if obj.user.role == "admin":
            print("permission2")
            return True
        else:
            print("permission3")
            return False