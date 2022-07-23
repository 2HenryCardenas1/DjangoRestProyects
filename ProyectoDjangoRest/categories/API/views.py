from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.API.serializer import CategorySerializer
from categories.API.permissions import IsAdminOnReadOnly
# esta libreria hay que instalar
from django_filters.rest_framework import DjangoFilterBackend


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOnReadOnly]
    serializer_class = CategorySerializer
    # Filtro para que me traiga todas las categorias publicadas o no
    #queryset = Category.objects.all()
    # Filtro para que solo me devuelva elementos publicados
    queryset = Category.objects.filter(published=True)
    #Lookup_field es para indicarle por que dato buscar y actualziar (predefinido ID)
    lookup_field = 'slug'
    # Filtro con django_filters (no se recomienda pra url): uso = url/?published=condicion
    """filter_backends = [DjangoFilterBackend]
    # Aca se le indica los parametros el cual quereamos filtar
    filterset_fields = ['published']"""
