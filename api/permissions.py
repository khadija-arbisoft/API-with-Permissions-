

from rest_framework import permissions

class ModelPermissionsByMethod(permissions.BasePermission):
    """
    Custom permission to check if a user has permission to perform an action
    based on the HTTP method of the request.
    """

    def has_permission(self, request, view):
        # Mapping of HTTP methods to Django model permissions
        perms_map = {
            'GET': 'view_',
            'OPTIONS': 'view_',
            'HEAD': 'view_',
            'POST': 'add_',
            'PUT': 'change_',
            'PATCH': 'change_',
            'DELETE': 'delete_',
        }

        # Get the appropriate permission based on the HTTP method
        required_perm = perms_map.get(request.method)
        if required_perm:
            # Build the full permission name based on the view's model
            model_name = view.queryset.model._meta.model_name
            full_permission = f"{required_perm}{model_name}"

            # Check if the user has this permission
            return request.user.has_perm(f"{view.queryset.model._meta.app_label}.{full_permission}")

        return False