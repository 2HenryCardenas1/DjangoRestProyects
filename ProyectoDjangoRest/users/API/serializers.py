# Los serializadores sirven para gestioanr los datos que entrean y salen en las peticiones
from rest_framework import serializers
from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # datos que se necesitan para crear un usuario
        fields = [
            'id',
            'email',
            'username',
            'password'
        ]

    # Para la encriptacion(sha256) de la contraseña se modifica el metodo create

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            # Aca encriptamos la password
            instance.set_password(password)
        instance.save()
        return instance


# Obtener datos del usuario registrado
class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name'
        ]


# Actualizar datos Usuario

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
        ]


# Actualizar contraseña
class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
