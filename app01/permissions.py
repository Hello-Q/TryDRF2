from rest_framework import permissions

#
# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     自定义权限只允许对象所有者才编辑
#     """
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.operator == request.user
