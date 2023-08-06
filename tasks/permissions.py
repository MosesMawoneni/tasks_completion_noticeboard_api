from rest_framework import permissions

# The class `IsPlannerOrReadOnly` is a custom permission class in Django that allows only
# authenticated users with the role of "planner" to have permission to perform certain actions, while
# allowing all users to have read-only access.
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
    
# The class `IsWorkerOrReadOnly` is a custom permission class in Django that allows authenticated
# users to perform safe methods and only allows the worker of an object to perform other methods.
class IsWorkerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request,view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.worker == request.user