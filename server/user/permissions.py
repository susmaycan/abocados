from rest_framework.permissions import BasePermission

from user.models import User


class IsStandardUser(BasePermission):
    def has_permission(self, request, view):
        try:
            User.objects.get(email=request.user)
        except User.DoesNotExist:
            return False
        return True


class IsOwnUser(BasePermission):
    def has_permission(self, request, view):
        try:
            user_id = request.resolver_match.kwargs.get("pk")
            User.objects.get(id=user_id)
            if int(user_id) != request.user.id:
                return False
        except User.DoesNotExist:
            pass
        return True


class IsOwnUserNested(BasePermission):
    def has_permission(self, request, view):
        try:
            user_id = request.resolver_match.kwargs.get("user_pk")
            User.objects.get(id=user_id)
            if int(user_id) != request.user.id:
                return False
        except User.DoesNotExist:
            pass
        return True
