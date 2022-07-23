from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from users.API.serializers import UserRegisterSerializer, UserViewSerializer, UserUpdateSerializer, \
    ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from users.models import User


# Registro de usaurios
class RegisterView(APIView):

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # Si es valido guardeme el user
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Metodo que nos sirve para obtener y actualizar el usuario
class UserView(APIView):
    # Permiso para que estas opciones la puedan hacer usuarios ya registrados
    permission_classes = [IsAuthenticated]

    #  Obtener datos del usuario registrado
    def get(self, request):
        serializer = UserViewSerializer(request.user)
        return Response(serializer.data)

    # Actualizar
    def put(self, request):
        # traemos el id del request
        user_id = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user_id, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Actualizar contraseña
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Verificamos la contraseña actual
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password hace la encriptacion de la nueva contraseña
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
