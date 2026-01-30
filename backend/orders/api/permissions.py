from rest_framework.permissions import BasePermission

class IsOrderOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        # obj is a instance of Order
        return obj.user == request.user
