from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsCompanyManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.company is not None and request.user.is_manager


class IsSameCompany(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.company == obj.company


class IsObjInACompany(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.company is not None


class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
