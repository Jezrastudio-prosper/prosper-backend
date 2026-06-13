"""
DRF permission classes controlling access to API endpoints.

Docs: https://www.django-rest-framework.org/api-guide/permissions/

Rules:
    - Inherit from BasePermission only — no view mixins in this file.
    - has_permission: request-level gate (can this user use this endpoint at all?).
    - has_object_permission: object-level gate (can this user act on this specific object?).
    - Never query the database beyond what is needed to make the access decision.
    - Apply via permission_classes on the view or globally in settings.

Example:
    class IsOwnerOrReadOnly(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj.owner == request.user
"""
