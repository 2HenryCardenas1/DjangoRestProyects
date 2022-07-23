from rest_framework import serializers
from users.API.serializers import UserViewSerializer
from categories.API.serializer import CategorySerializer
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    # Aca obtenemos los datos del usuario que creo el post
    user = UserViewSerializer()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'slug',
            'miniature',
            'published',
            'created_at',
            'user',
            'category'
        ]
