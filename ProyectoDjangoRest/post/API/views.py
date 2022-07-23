from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.API.serializers import PostSerializer
from post.API.permissions import IsAdminOnReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOnReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    # Filtrar por la categoria del post
    # filterset_fields = ['category']
    # Filtrar por el slug de la categoria del post
    filterset_fields = ['category__slug']
