from rest_framework import permissions
from django.contrib.auth import get_user_model

class IsAdminToAffect(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            if request.user == get_user_model().id:
                return True
    # def has_object_permission(self, request, view, obj):
        
    #     return 