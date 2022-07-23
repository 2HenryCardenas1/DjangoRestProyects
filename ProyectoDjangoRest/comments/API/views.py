from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from comments.models import Comment
from comments.API.serializers import CommentSerilizer
from comments.API.permissions import IsOwnerOrReadAndCreateOnly


class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerilizer
    queryset = Comment.objects.all()
    # Ordenar los comentarios de manera decendente segun la fecha
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    # Se le indica con un - para que sea de manera descendente
    ordering = ['-created_At']

    # Filtar comentarios por post usando DjangoFilterBackend
    filterset_fields = ['post']
