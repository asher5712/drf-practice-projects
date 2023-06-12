from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS

class IsAdminOrReadOnly(IsAdminUser):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_staff)
    
class IsReviewUserorReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user or request.user.is_staff