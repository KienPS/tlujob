from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS

from job_recruitment.models import *


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsInACompany(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.company is not None


class IsCompanyOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.job.company == request.user.company and request.user.is_manager
