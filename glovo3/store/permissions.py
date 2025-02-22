from rest_framework import permissions


class CheckCreateStore(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'owner':
            return True
        return False


class CheckOwnerStore(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.owner


class CheckCreateAllProduct(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'owner':
            return True
        return False


class CheckOwnerAllProduct(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.store.owner


# class CheckCreateProductCombo(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.user_role == 'owner':
#             return True
#         return False
#
#
# class CheckOwnerProductCombo(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return request.user == obj.store.owner


class CheckCreateOrder(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'client':
            return True
        return False


class CheckOwnerOrder(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.client


class CheckCreateCourier(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'courier':
            return True
        return False


class CheckOwnerCourier(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user.user_role


class CheckReviewCourier(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'courier':
            return False
        return True