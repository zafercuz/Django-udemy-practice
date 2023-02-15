from rest_framework import permissions

from watchlist_app.models import Review


class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return super().has_permission(request, view)


class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Review):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.review_user == request.user
