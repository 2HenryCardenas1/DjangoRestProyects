from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import status
from post.models import Post
from post.API.serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from post.API.permission import IsAdminOrReadOnly


# Con el ModelViewSet se puede crear directamente
# todo el CRUD, con este tambien se puede editar directamente los metodos
# y especificar que tipo de metodo se quiere hacer get,post,put,delete

class PostModelViewSet(ModelViewSet):
    # Aca le indicamos que solo los usuarios que tengan un token de sesion pueden hacer uso de esta clase
    # permission_classes = [IsAuthenticated]
    # Aca le indicamos que solo los usuarios ADMINISTRADORES pueden hacer uso de esta clase
    # permission_classes = [IsAdminUser]
    # Con este permiso le indicamos que todos los usaurios podran leer los datos pero
    # los autenticados podran acceder al CRUD
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # Usando nuestro permiso creado
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # Asi se le especifica que metodo del CRUD queremos que nos realice
    # http_method_names = ['get']


# APIView contiene los metodos

"""class PostApiView(APIView):

    # Este metodo devuelve los datos
    def get(self, request):
        # many=True es para que me devuelva el array completo de mis datos
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    # Endpoint para crear nuevos post
    def post(self, request):
        # Obtenemos los datos enviados por post
        serializer = PostSerializer(data=request.POST)
        # Validamos que lso datos sean validos
        serializer.is_valid(raise_exception=True)
        # Guardamos
        serializer.save()
        # Retornamos un response con un estado 200OK y enviamos la dara
        return Response(status=status.HTTP_200_OK, data=serializer.data)"""

"""class PostViewSet(ViewSet):

    # Este metodo devuelve los datos
    def list(self, request):
        # many=True es para que me devuelva el array completo de mis datos
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    # Endpoint para crear nuevos post
    def create(self, request):
        # Obtenemos los datos enviados por post
        serializer = PostSerializer(data=request.POST)
        # Validamos que lso datos sean validos
        serializer.is_valid(raise_exception=True)
        # Guardamos
        serializer.save()
        # Retornamos un response con un estado 200OK y enviamos la dara
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    # Endpoint para traer un dato segun ID

    def retrieve(self, request, pk):
        post = PostSerializer(Post.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=post.data)"""
