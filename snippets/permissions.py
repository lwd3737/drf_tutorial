from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    객체의 owner에게만 편집 권한 부여
    '''
    def has_object_permission(self, request, view, obj):
        #GET, HEAD, OPTIONS request - read-only
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user

