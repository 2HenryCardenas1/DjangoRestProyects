from rest_framework.permissions import BasePermission
from comments.models import Comment


class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            # traemos el id del comentario
            id_comment = view.kwargs['pk']
            # Obtenemos los datos del comentario
            comment = Comment.objects.get(pk=id_comment)
            # Traemos el id del usuario que esta ejecutando la peticion
            id_user = request.user.pk
            # Sacamos el id del usuario que creo el comentario
            id_user_comment = comment.user_id
            # Comprobamos que el id del usuario que hace la peticion sea igual al id del user que lo creo
            if id_user == id_user_comment:
                return True

            return False
