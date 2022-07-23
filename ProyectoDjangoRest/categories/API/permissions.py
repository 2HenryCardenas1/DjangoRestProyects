from rest_framework.permissions import BasePermission


class IsAdminOnReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Caulquier usuario que haga peticion GET se le mostrara la info
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff
