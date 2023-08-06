from rest_framework import permissions

class IsPlannerOrReadOnly(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.user.is_authenticated:
          if request.user.role == 'planner':
                return True
          return False
        
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.worker == request.user
    
class IsWorkerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request,view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.worker == request.user