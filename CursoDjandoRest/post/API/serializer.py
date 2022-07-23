from rest_framework.serializers import ModelSerializer
from post.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        # le pasamos los datos que queremos usar al momento de hacer la peticion
        fields = ['title', 'description']
