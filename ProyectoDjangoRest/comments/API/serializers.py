from rest_framework import serializers
from comments.models import Comment


class CommentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content',
            'created_At',
            'user',
            'post'

        ]
